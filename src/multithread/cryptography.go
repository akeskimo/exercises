package main

import (
	"fmt"
	"flag"
	"os"
	"io/ioutil"
	"io"
	"crypto/aes"
	"crypto/cipher"
	"crypto/md5"
	"crypto/rand"
	"encoding/hex"
)

func createHash(key string) (string, error) {
	hasher := md5.New()
	_, err := hasher.Write([]byte(key))
	if err != nil {
		return "", err
	}
	hash := hex.EncodeToString(hasher.Sum(nil))
	return hash, nil
}

func encrypt(data []byte, passphrase string) ([]byte, error) {
	var ciphertext []byte
	key, err := createHash(passphrase);
	if err != nil {
		return ciphertext, err
	}
	block, err := aes.NewCipher([]byte(key))
	if err != nil {
		return ciphertext, err
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return ciphertext, err
	}
	nonce := make([]byte, gcm.NonceSize())
	if _, err = io.ReadFull(rand.Reader, nonce); err != nil {
		return ciphertext, err
	}
	ciphertext = gcm.Seal(nonce, nonce, data, nil)
	return ciphertext, nil
}

func decrypt(data []byte, passphrase string) ([]byte, error) {
	var plaintext []byte
	key, err := createHash(passphrase)
	if err != nil {
		return plaintext, err
	}
	block, err := aes.NewCipher([]byte(key))
	if err != nil {
		return plaintext, err
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return plaintext, err
	}
	nonceSize := gcm.NonceSize()
	nonce, ciphertext := data[:nonceSize], data[nonceSize:]
	plaintext, err = gcm.Open(nil, nonce, ciphertext, nil)
	if err != nil {
		return plaintext, err
	}
	return plaintext, nil
}

func encryptFile(filename string, data []byte, passphrase string) error {
	ciphertext, err := encrypt(data, passphrase)
	if err != nil {
		return err
	}
	f, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = f.Write(ciphertext)
	if err != nil {
		return err
	}
	return nil
}

func decryptFile(filename string, passphrase string) ([]byte, error) {
	var plaintext []byte
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return plaintext, err
	}
	plaintext, err = decrypt(data, passphrase)
	if err != nil {
		return plaintext, err
	}
	return plaintext, err
}

var (
	mode = flag.String("mode", "", "Choose 'encrypt' or 'decrypt'")
	data = flag.String("data", "", "Plaintext/ciphertext to be encrypted/decrypted")
	filepath = flag.String("filepath", "", "Filepath that will contain the encrypted/decrypted data")
	password = flag.String("password", "", "Password used for the encryption.")
)

func init() {
	flag.Parse()
}

func exitWithError(err error) {
	fmt.Fprintf(os.Stderr, "error: %+v\n", err)
	os.Exit(1)
}

func main() {
	if *mode == "encrypt" {
		if *data == "" {
			exitWithError(fmt.Errorf("No data given to encrypt"))
		}
		err := encryptFile(*filepath, []byte(*data), *password)
		if err != nil {
			exitWithError(err)
		}
	} else if *mode == "decrypt" {
		plaintext, err := decryptFile(*filepath, *password)
		if err != nil {
			exitWithError(err)
		}
		fmt.Printf("%s", plaintext)
	} else {
		exitWithError(fmt.Errorf("Invalid mode: %v", mode))
		os.Exit(1)
	}
}
