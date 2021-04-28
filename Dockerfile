# Create an intermediate image to install requirements
FROM databricksruntime/standard:6.0.x-scala2.11 as intermediate-build

# Install job package requirements
SHELL ["/bin/bash", "-c"]
COPY requirements.txt ./
COPY pip.conf ./
RUN /databricks/conda/bin/conda init bash && \
	eval "`/databricks/conda/bin/conda 'shell.bash' 'hook' 2> /dev/null`" && \
	conda activate dcs-minimal && \
	PIP_CONFIG_FILE="$(pwd)/pip.conf" \
	pip install -r requirements.txt
RUN rm ./pip.conf

FROM databricksruntime/standard:6.0.x-scala2.11

LABEL org.label-schema.name="poc-docker-databrics-il" \
      org.label-schema.description="ETL to generate New York taxi data" \
      org.label-schema.vcs-url="https://gitlab.infinitelambda.com/infinitelambda/poc-docker_pyspark_databricks_aws.git" \
      org.label-schema.usage="README.md" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.vendor="InfiniteLambda" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.version="${BUILD_NUMBER}"

# Copy installed packages from intermediate image
COPY --from=intermediate-build /databricks/conda/envs/dcs-minimal/lib/python3.7/site-packages/ /databricks/conda/envs/dcs-minimal/lib/python3.7/site-packages/

# Install the job source code
COPY . ./src_package
RUN /databricks/conda/bin/conda init bash && \
	eval "`/databricks/conda/bin/conda 'shell.bash' 'hook' 2> /dev/null`" && \
	conda activate dcs-minimal && \
	pip install src_package/