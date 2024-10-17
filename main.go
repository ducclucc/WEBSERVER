package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		fmt.Println("GET request received for path:", r.URL.Path)
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("GET request logged\n"))

	case http.MethodPost:
		body, err := ioutil.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "Unable to read request body", http.StatusBadRequest)
			return
		}
		defer r.Body.Close()
		fmt.Println("POST request received for path:", r.URL.Path)
		fmt.Println("Request body:", string(body))
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("POST request logged\n"))

	default:
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}

func main() {
	http.HandleFunc("/", handler)

	fmt.Println("Server listening on http://0.0.0.0:10000")
	if err := http.ListenAndServe("0.0.0.0:10000", nil); err != nil {
		fmt.Println("Error starting server:", err)
	}
}
