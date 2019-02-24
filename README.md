# Build your ceph fs kernel driver

```
mkdir ceph-4.4.52

cd ceph-4.4.52

git clone https://github.com/xcp-ng/xcp-ng-build-env

git clone https://github.com/rushikeshjadhav/ceph-4.4.52

chown 1000 ./ceph-4.4.52/ -R

./xcp-ng-build-env/run.py -b 7.6 --build-local ceph-4.4.52/ --rm
```
