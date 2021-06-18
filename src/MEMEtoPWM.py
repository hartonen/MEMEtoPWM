#!/usr/bin/env python
import argparse

import numpy as np

def MEMEtoPWM():

    ########################
    #command line arguments#
    ########################

    parser = argparse.ArgumentParser()

    #MANDATORY PARAMETERS
    parser.add_argument("MEME", help="Full path to the input MEME-file.", type=str)
    #outdir = directory for output
    parser.add_argument("outdir", help="Full path to output directory where PWMs are saved. Motif names from the MEME-file are used as file names.", type=str)

    args = parser.parse_args()
    
    motif = None
    motif_found = False
    with open(args.MEME,'rt') as infile:
        for line in infile:
            line = line.strip()
            if len(line)<1: continue
            if line.count('MOTIF')>0:
                #this is the start of a new motif
                motif_found = True
                if motif is not None:
                    #saving the last motif to a file
                    print("saving "+motifname) 
                    np.savetxt(args.outdir+motifname+".pwm",np.transpose(np.array(motif)))
                motifname = line.replace(" ","-").strip()
                motif = []
            elif not motif_found: continue    
            elif line.count('letter')>0: continue
            elif line[0]=='*':
                #this means that all motifs have been read in
                break
            elif len(line)>0:
                #these are the lines containing the motif
                line = line.split()
                motif.append([float(i) for i in line])


#end
MEMEtoPWM()
