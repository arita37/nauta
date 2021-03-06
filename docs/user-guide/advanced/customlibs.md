# Installing Libraries and Dependencies

To install an OS library or dependency that _is not_ included in standard Nauta Docker image. It is required to modify draft pack definition. To install a pip dependency (like numpy or pandas), refer to `experiment submit` command documentation.

## Modifying Existing Draft Packs

The draft packs are located in the nctl_config_ folder. Navigate to _.draft/packs_ folder to list existing packs.
The default pack used by _nctl_ client is _tf-training-tfjob_. Edit the _Dockerfile_ located in selected pack to make necessary changes.

Example _Dockerfile_:

    FROM nauta/tensorflow:1.9.0-py3
    
    WORKDIR /app

    ADD training.py .
    
    ENV PYTHONUNBUFFERED 1
    

### Installing OS Packages

The images in Nauta are based on CentOS. To install system package add the following lines to _Dockerfile_:

    RUN yum update
    RUN yum install package1 package2

### Proxy

Depending on the network configuration it may be required to setup proxy servers.

     ARG http_proxy=corporate-proxy.com:911
     ARG https_proxy=corporate-proxy.com:912

### Example Dockerfile Modification

Below is an example _Dockerfile_ showing installation of additional packages.

  
    FROM nauta/tensorflow:1.9.0-py3
    
    WORKDIR /app

    ARG http_proxy=corporate-proxy.com:911
    ARG https_proxy=corporate-proxy.com:912
         
    RUN yum update
    RUN yum install libsndfile
    
    ADD training.py .
    
    ENV PYTHONUNBUFFERED 1
    
    
    
