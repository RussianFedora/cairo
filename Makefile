# Makefile for source rpm: cairo
# $Id$
NAME := cairo
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
