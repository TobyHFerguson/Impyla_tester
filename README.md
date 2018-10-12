# Implya tester

This image will test connecting implya to an ALtus DW secure cluster.

Execute thus:

```
docker run -it tobyhferguson/implya:latest user password hostip
```

where the `user`, `password`, `host` are the three fields `LDAP Username`, `LDAP Password` and `Coordinator Endpoint` taken from the Cluster Access Information pop-up (See [Getting the Credentials for an Altus Data Warehouse Cluster](https://www.cloudera.com/documentation/altus/topics/altdw_user_access.html#dw_get_cluster_credentials) for details)
