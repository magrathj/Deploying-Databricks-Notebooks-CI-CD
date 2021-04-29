# Deploying-Databricks-Notebooks-CI-CD
Using docker to deploy packages and notebooks using docker to an Azure Databricks workspace


```
    conda create --name pyspark-databricks-poc-test  
```

```
	conda activate pyspark-databricks-poc-test 
```


### Recreate env and run tests

```
    conda deactivate &&
    conda create -n pyspark-databricks-poc-test &&
    conda activate pyspark-databricks-poc-test &&
    pip install --upgrade pip &&
    pip install pip-tools &&
    make install-test
```

```
    docker build -t pyspark-databricks-poc .
```

```
    docker run exec -it pyspark-databricks-poc /bin/bash
```


## Reference
[Deploying databricks notebooks CI/CD with GitLabs](https://infinitelambda.com/post/deploying-databricks-notebooks-ci-cd-gitlab/)