#!/bin/bash
set -u
set -e
#-D__ANDROID_API__=$OPENSSL_ANDROID_API
export BUILD_ARCHS=${BUILD_ARCHS:-arm_32 arm_64 x86_64 x86_32}
#export OPENSSL_BRANCH=OpenSSL_1_1_1-stable
export OPENSSL_ANDROID_API=21

NDK=${1:-$NDK}

export ANDROID_NDK_HOME=$NDK

export BASE=$(realpath ${BASE:-$(pwd)})

export PREFIX=$BASE/prefix

if [ -d $PREFIX ]; then
    echo "Target folder exists. Remove $PREFIX to rebuild"
    exit 1
fi

mkdir -p $PREFIX

cd $BASE
if [ ! -d openssl ]; then
    git clone --depth 1 git://git.openssl.org/openssl.git
fi
cd openssl
echo "Building OpenSSL in $(realpath $PWD), deploying to $PREFIX"

export PATH=$NDK/toolchains/llvm/prebuilt/linux-x86_64/bin:$PATH

if [[ "$BUILD_ARCHS" = *"arm_32"* ]]; then
    ./Configure shared android-arm  --prefix=$PREFIX/armeabi-v7a
    make clean
    make -j$(nproc) CALC_VERSIONS="SHLIB_COMPAT=; SHLIB_SOVER="  build_libs
    make -j$(nproc) install_sw
fi

if [[ "$BUILD_ARCHS" = *"arm_64"* ]]; then
    ./Configure shared android-arm64 --prefix=$PREFIX/arm64-v8a
    make clean
 #   make depend
    make -j$(nproc) CALC_VERSIONS="SHLIB_COMPAT=; SHLIB_SOVER=" build_libs
    make -j$(nproc) install_sw
fi

if [[ "$BUILD_ARCHS" = *"x86_32"* ]]; then
    ./Configure shared android-x86  --prefix=$PREFIX/x86
    make clean
#    make depend
    make -j$(nproc) CALC_VERSIONS="SHLIB_COMPAT=; SHLIB_SOVER="  build_libs
    make -j$(nproc) install_sw
fi

if [[ "$BUILD_ARCHS" = *"x86_64"* ]]; then
    ./Configure shared android-x86_64 --prefix=$PREFIX/x86_64
    make clean
#    make depend
    make -j$(nproc) CALC_VERSIONS="SHLIB_COMPAT=; SHLIB_SOVER=" build_libs
    make -j$(nproc) install_sw
fi
 
