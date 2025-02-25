# This is a basic Python application to encrypt and decrypt TXT, DOCX, and pdf files.
- This project was basically developed to experiment on the CI/CD pipeline automation.
- For more details, you can check the automation.yml in the workflows folder

## Using Docker (recommended)

```bash
docker pull iswnischay/aes-app
```
```bash
docker run -it iswnischay/aes-app
```
## Installation locally

```bash
git clone https://www.github.com/iswnischay/AES.git
```
```bash
pip install cryptodome
```
```bash
python3 aes.py
```
### To paste your file inside a container

- First run the container
- Then while running a container open another cmd/terminal ad use docker ps
- then get the container id (container id changes for every time you run the image)
 ```bash
docker cp eg.txt cid:/app/eg.txt
```
 ### To get your file from the container
- Here the image has stopped running so running the image again will make sure the old changes has not happened so use the old container id 
- use docker ps -a or you can use the same id which was used to paste the file from your local to the container 
- then get the container id (container id changes for every time you run the image)
 ```bash
docker cp cid:/app/eg.txt ./eg.txt
```
