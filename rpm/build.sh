#!/bin/bash -eux

# dbttools version
VERSION="0.3.0"
TAG="v0.3.0"

dnf update -y
dnf install rpm-build redhat-rpm-config yum-utils -y
dnf install git cmake gcc gcc-c++ make  -y
yum-builddep -y /workspace/rpm/dbttools.spec
git clone https://github.com/osdldbt/dbttools.git /tmp/dbttools
cd /tmp/dbttools
git archive --format=tar.gz --prefix=dbttools-${VERSION}/ ${TAG} > /workspace/dbttools-${VERSION}.tar.gz
cd /

rpmbuild \
	--clean \
	--define "pkgversion ${VERSION}" \
	--define "_topdir ${PWD}/tmp/rpm" \
	--define "_sourcedir ${PWD}/workspace" \
	-bb /workspace/rpm/dbttools.spec

rm /workspace/dbttools-${VERSION}.tar.gz
mkdir -p ${PWD}/workspace/rpm/build/
cp ${PWD}/tmp/rpm/RPMS/*/*.rpm ${PWD}/workspace/rpm/build/.
ls -lha ${PWD}/workspace/rpm/build/*.rpm
