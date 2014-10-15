# Unix Makefile for lexyacc example

MAINDIR=..
LYDIR=../lexyacc
INSTALLDIR=$(HOME)/bin
MOSMLC=mosmlc -c -I $(LYDIR)
MOSMLL=mosmlc
MOSMLLEX=mosmllex
MOSMLYACC=mosmlyac
MG_EXE=modelgen.exe
TG_EXE=tracegen.exe

all: parser.uo tparser.uo

install:
	

.SUFFIXES :
.SUFFIXES : .sml .sig .ui .uo .mlp .lex .c .o

.sig.ui:
	$(MOSMLC) $<

.sml.uo:
	$(MOSMLC) $<

clean:
	-rm -f *~
	-rm -f *.ui *.uo
	-rm -f $(MG_EXE) $(TG_EXE)
	-rm -f Makefile.bak

