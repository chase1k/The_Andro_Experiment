#
## For more information about using CMake with Android Studio, read the
## documentation: https://d.android.com/studio/projects/add-native-code.html.
## For more examples on how to use CMake, see https://github.com/android/ndk-samples.
#
## Sets the minimum CMake version required for this project.
#cmake_minimum_required(VERSION 3.22.1)
#
## Declares the project name. The project name can be accessed via ${ PROJECT_NAME},
## Since this is the top level CMakeLists.txt, the project name is also accessible
## with ${CMAKE_PROJECT_NAME} (both CMake variables are in-sync within the top level
## build script scope).
#project("andro")
#
## Creates and names a library, sets it as either STATIC
## or SHARED, and provides the relative paths to its source code.
## You can define multiple libraries, and CMake builds them for you.
## Gradle automatically packages shared libraries with your APK.
##
## In this top level CMakeLists.txt, ${CMAKE_PROJECT_NAME} is used to define
## the target library name; in the sub-module's CMakeLists.txt, ${PROJECT_NAME}
## is preferred for the same purpose.
##
#
#find_package(openssl REQUIRED CONFIG)
#
## In order to load a library into your app from Java/Kotlin, you must call
## System.loadLibrary() and pass the name of the library defined here;
## for GameActivity/NativeActivity derived applications, the same library name must be
## used in the AndroidManifest.xml file.
#add_library(${CMAKE_PROJECT_NAME} SHARED
#    # List C/C++ source files with relative paths to this CMakeLists.txt.
#        rollcode.cpp)
#
## Specifies libraries CMake should link to your target library. You
## can link libraries from various origins, such as libraries defined in this
## build script, prebuilt third-party libraries, or Android system libraries.
#
#target_link_libraries(${CMAKE_PROJECT_NAME} openssl::openssl)
#
#target_link_libraries(${CMAKE_PROJECT_NAME}
#    # List libraries link to the target library
#    android
#    log)

cmake_minimum_required(VERSION 3.22.1)

project("andro")


#set(OPENSSL_SSL_DIR ../jniLibs/x86_64/)
#set(OPENSSL_INCLUDE_DIR ../jniLibs/x86_64/)
#set(OPENSSL_CRYPTO_LIBRARY ../jniLibs/x86_64/l)
#set(OPENSSL_ROOT_DIR ../cpp/openssl)
#set(OPENSSL_ROOT_DIR ../jniLibs/)
#set(OPENSSL_ROOT_DIR ${CMAKE_CURRENT_LIST_DIR}/../../../../prefix/${CMAKE_ANDROID_ARCH_ABI})

SET(distribution_DIR ${CMAKE_SOURCE_DIR}/../../../../prefix)
SET(OPENSSL_ROOT_DIR ${distribution_DIR}/${ANDROID_ABI})

SET(OPENSSL_LIBRARIES_DIR "${OPENSSL_ROOT_DIR}/lib")
SET(OPENSSL_INCLUDE_DIR ${OPENSSL_ROOT_DIR}/include)
SET(OPENSSL_LIBRARIES "ssl" "crypto")
# Find the OpenSSL libraries
#find_library(SSL_LIBRARY ssl HINTS ${OPENSSL_SSL_DIR})
#find_library(CRYPTO_LIBRARY crypto HINTS ${OPENSSL_CRYPTO_DIR})

#find_package(OpenSSL REQUIRED)


#find_library(SSL_LIBRARY ssl)
#find_library(CRYPTO_LIBRARY crypto)

#if(NOT SSL_LIBRARY OR NOT CRYPTO_LIBRARY)
#    message(FATAL_ERROR "OpenSSL libraries not found.")
#endif()
LINK_DIRECTORIES(${OPENSSL_LIBRARIES_DIR})

add_library(${CMAKE_PROJECT_NAME} SHARED
        rollcode.cpp)

#target_link_libraries(${CMAKE_PROJECT_NAME} OpenSSL::SSL)
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC ${OPENSSL_INCLUDE_DIR})
# Link your project's shared library against the OpenSSL libraries
#target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE ${SSL_LIBRARY} ${CRYPTO_LIBRARY})

# Link your project's shared library against other required libraries
target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE android log ${OPENSSL_ROOT_DIR}/lib/libssl.so ${OPENSSL_ROOT_DIR}/lib/libcrypto.so )

#target_link_libraries(${CMAKE_PROJECT_NAME} ${SSL_LIBRARY} ${CRYPTO_LIBRARY})
#
#target_link_libraries(${CMAKE_PROJECT_NAME}
#        android
##        ${OPENSSL_LIBRARIES}
#        log)
