<h1>This is a basic Python application to encrypt and decrypt TXT, DOCX, and pdf files.</h1>
<h4>This project was basically developed to experiment on the CI/CD pipeline automation. For more details, you can check the automation.yml in the workflows folder</h4>
<h3>Installation locally</h3>
<ul>
<li>git clone </li>
<li>pip install cryptodome</li>
<li>python3 aes.py</li>
</ul>
<h3>using docker (recommended)</h3>
<ul>
<li>docker pull iswnischay/aes-app</li>
<li>docker run -it iswnischay/aes-app</li>
</ul>
<h3>To paste your file inside a container</h3>
<ul>
<li>First run the container</li>
<li>Then while running a container open another cmd/terminal ad use docker ps</li>
<li>then get the container id (container id changes for every time you run the image)</li>
<li> docker cp eg.txt cid:/app/eg.txt</li>
</ul>
<h3> to get your file from the container</h3>
<ul>
<li>Here the image has stopped running so running the image again will make sure the old changes has not happened so use the old container id </li>
<li>use docker ps -a or you can use the same id which was used to paste the file from your local to the container </li>
<li>then get the container id (container id changes for every time you run the image)</li>
<li> docker cp cid:/app/eg.txt ./eg.txt</li>
</ul>
