### How to set up the NLP code in your own AWS instance
# NLP Web API Service 

This project is for creating a web API that will provide users with NLP data on submitted data.
We have crated & deployed this application as a flask application.

## Getting Started

These instructions will get you a copy of the project up and running on your own AWS machine for development and testing purposes. 

### Prerequisites

We assume that an AWS ec2 instance has been created. For more details on this please refer to the AWS user guide here-
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html


### Installing

A step by step series of commands to get you env running

Preparing the AWS instance. First you need to have super user permissions to create folders-

```
sudo su
```

Now we begin by installing git and Python 3 if they are not already present 

```
yum install git
yum install python36
```

We need to install new python packages with help of pip. So lets install pip.

```
sudo easy_install pip
```

If the installation is successful, you will be able to check the version of pip

```bash
pip --version
```

If this gives an error then we can try an alternate command 

```bash
python3 --version
sudo apt-get install python-pip
```
This command might work, but if does not we need to download & install pip and setup PATH variable to get pip working.
Use the following commands -
 
```
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip --version
```

It is possible that the AWS instance Linux version still gives error for pip after this

follow the below steps to add the installation path of pip to the PATH variable 

```bash
echo $PATHecho $PATH
export PATH=~/.local/bin:$PATH
echo $PATH
pip --version
```

Now we are ready to install the required libraries -

```bash
pip install requests

pip install textblob

python3 -m textblob.download_corpora

pip install flask-restplus

pip install pandas
```
We have made the code available in a git repo. Clone to repository and get the code

```bash
git clone https://github.com/Brajam/MidTerm.git
ls -ltr
cd MidTerm/
ls -ltr
```

Now lets try to run the flask application- 
```
python3 midterm.py
[root@ip-172-31-43-40 MidTerm]# python3 midterm.py
 * Serving Flask app "midterm" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)

```

Now the applcation is  up and running. 

## Running the tests

You can look at the application swagger file using the base link -
http://<ec2-instance-host>:8080/

You can call the various end points as described in the swagger UI


## Built With

* [Flask](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Git](https://maven.apache.org/) - Code management
* [Textblob](https://textblob.readthedocs.io/en/dev/install.html) - Used to create the NLP services
* [Flask RestPlus](https://flask-restplus.readthedocs.io/en/stable/installation.html) - Generating the Swagger UI


## Acknowledgments & Notes

* Text Blob NLP API has been extremely useful and well documented. 
* [Amazon web serivices](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-proxy-with-ssm-agent-al-python-requests.html) Documentation is very useful for trobleshooting. But, just need to know how to get around to the correct link of the documentation.
