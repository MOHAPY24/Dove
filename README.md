# **Dove**

### **A Protocol for Running Ollama Remotely**

## **Overview**

**Dove** is a lightweight protocol designed to run **Ollama models remotely** over standard HTTP.
It provides a simple and developer-friendly interface for sending prompts, receiving responses, and performing model operations from any machine on your network—or across the internet.

Built with **Python**, using `requests` for the client side and **Flask** for the server side, Dove aims to offer a minimal, easy-to-extend environment for remote AI execution without the overhead of heavyweight RPC systems.

## **Features**

* 🔌 **Remote execution of Ollama models** over HTTP
* 🐍 **Python-based implementation** using Flask & Requests
* 📦 **Simple setup, minimal dependencies**
* 🌐 **Designed for extensibility** — add routes, middleware, caching, auth, etc.
* 🤝 **Compatible with your existing Ollama workflows**

## **How It Works**

Dove exposes an HTTP interface that:

1. Receives prompts or model instructions from a remote client
2. Forwards them to a local Ollama instance
3. Returns the model’s output as a structured JSON response

This makes it easy to:

* Run models from lightweight devices
* Offload inference to more powerful machines
* Integrate Ollama into distributed systems
* Build custom remote AI backends

## **Installation**

```bash
git clone https://github.com/MOHAPY24/Dove
cd Dove
pip install -r requirements.txt
```

## **Usage**

### **Start the Dove server** if your hosting a model.

```bash
python server/app.py
```

### **Send a request from a client**

Edit the client/configs/session.jsonc and client/configs/user.jsonc file and add your prompt in the data variable where it says prompt
then for a CLI helper (you can code your own system using the class in `client/dove.py`)

```bash
python3 client/client.py
```

## **Roadmap**

* [ ] Authentication support
* [ ] Streaming responses
* [ ] Model listing & management endpoints
* [ ] Optional encryption layer
* [ ] Multi-model queueing system

## **Contributing**

Pull requests, feature suggestions, and general improvements are welcome!
Feel free to open an issue to discuss any changes.

## **License**

Licensed under the **MIT License**.
See the full text in [`LICENSE`](LICENSE).
