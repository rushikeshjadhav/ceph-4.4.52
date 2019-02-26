#
# Makefile for CEPH filesystem.
#

obj-m += ceph.o

ceph-y := super.o inode.o dir.o file.o locks.o addr.o ioctl.o \
	export.o caps.o snap.o xattr.o \
	mds_client.o mdsmap.o strings.o ceph_frag.o \
	debugfs.o

ceph-n += cache.o
ceph-n += acl.o
