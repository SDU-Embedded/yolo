'''
Created on Feb 20, 2017
Original author: jumabek

Modified on April 2, 2017
Modified by: MathiasThor
'''
import os
import sys
import argparse
import StringIO

def convert_anchors(anchor_file,new_res):

    f = open(anchor_file)
    lines = [line.rstrip('\n') for line in f.readlines()]

    if len(lines)<2:
        print 'Your anchor file contains less than 2 lines, please provide the correct format\n';
        exit()

    f.close()

    old_res = (416,416)
    (o_w,o_h) = map(int,old_res)

    biases = lines[0].split(',')
    biases = map(float,biases)
    (n_w,n_h) = new_res

    for i in range(len(biases)/2):
        biases[2*i] = biases[2*i]/o_w*n_w
        biases[2*i+1] = biases[2*i+1]/o_h*n_h

    output = StringIO.StringIO()

    output.write('New Anchors: ')

    for i in range(len(biases)/2-1):
        output.write('%f,%f, '%(biases[2*i],biases[2*i+1]))

    #there should not be comma after last anchor, that's why
    output.write('%f,%f\n'%(biases[2*(len(biases)/2-1)],biases[2*(len(biases)/2-1)+1]))

    # output.write('%s\n'%lines[1])
    print output.getvalue()
    print "Copy these into the yolo_obj.cfg file (after 'anchors=')"

parser = argparse.ArgumentParser()

parser.add_argument('-anchor_file', required = True,  help='path to input anchor\n' )

parser.add_argument('-n_w', required = True, type = int,
                    help='new res width\n' )
parser.add_argument('-n_h', required = True, type = int,
                    help='new res height\n' )

args = parser.parse_args()

convert_anchors(args.anchor_file,(args.n_w,args.n_h))
