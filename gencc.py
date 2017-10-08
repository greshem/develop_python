#!/usr/bin/python

"""
gencc: A simple program to generate credit card numbers that pass the MOD 10 check
(Luhn formula).
Usefull for testing e-commerce sites during development.

Copyright 2003 Graham King

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

Modded for w3af.
"""

from random import Random
import sys
import copy
import getopt
try:
    import core.controllers.outputManager as om
except:
    class om:
        class out:
            def information( str ):
                print '\r' + str
            information = staticmethod(information)

visaPrefixList = [  ['4', '5', '3', '9'], 
                    ['4', '5', '5', '6'], 
                    ['4', '9', '1', '6'],
                    ['4', '5', '3', '2'], 
                    ['4', '9', '2', '9'],
                    ['4', '0', '2', '4', '0', '0', '7', '1'],
                    ['4', '4', '8', '6'],
                    ['4', '7', '1', '6'],
                    ['4'] ]

mastercardPrefixList = [    ['5', '1'],
                            ['5', '2'],
                            ['5', '3'],
                            ['5', '4'],
                            ['5', '5'] ]

amexPrefixList = [  ['3', '4'],
                    ['3', '7'] ]

discoverPrefixList = [ ['6', '0', '1', '1'] ]

dinersPrefixList = [    ['3', '0', '0'],
                        ['3', '0', '1'],
                        ['3', '0', '2'],
                        ['3', '0', '3'],
                        ['3', '6'],
                        ['3', '8'] ]

enRoutePrefixList = [   ['2', '0', '1', '4'],
                        ['2', '1', '4', '9'] ]

jcbPrefixList16 = [   ['3', '0', '8', '8'],
                    ['3', '0', '9', '6'],
                    ['3', '1', '1', '2'],
                    ['3', '1', '5', '8'],
                    ['3', '3', '3', '7'],
                    ['3', '5', '2', '8'] ]

jcbPrefixList15 = [ ['2', '1', '0', '0'],
                    ['1', '8', '0', '0'] ]

voyagerPrefixList = [ ['8', '6', '9', '9'] ]                    
                    

"""
'prefix' is the start of the CC number as a string, any number of digits.
'length' is the length of the CC number to generate. Typically 13 or 16
"""
def completed_number(prefix, length):

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = generator.choice(['0',  '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        ccnumber.append(digit)


    # Calculate sum 

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int( reversedCCnumber[pos] ) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int( reversedCCnumber[pos+1] )

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append( str(checkdigit) )
    
    return ''.join(ccnumber)

def credit_card_number(generator, prefixList, length, howMany):

    result = []

    for i in range(howMany):
        ccnumber = copy.copy( generator.choice(prefixList) )
        result.append( completed_number(ccnumber, length) )

    return result

def output(title, numbers):
    result = []
    result.append('Generated ' + title + ' card:')
    result.append( '\n'.join(numbers) )
    result.append( '' )
    return '\n'.join(result).strip()

generator = Random()
generator.seed()        # Seed from current time

types = ['mastercard','visa16','visa13','amex','discover','diners','enRoute','jcb15','jcb16','voyager']

def usage():
    om.out.information('w3af - Credit Card Generator, original version: Graham King')
    om.out.information('')
    om.out.information('Options:')
    om.out.information('    -h  Print this help message.')
    om.out.information('    -t  Type of CC to generate:')
    for type in types:
        om.out.information('        - ' + type)
    om.out.information('')

#
# Main
#
def main():
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:", ["help", "type"])
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    type = None
    for o, a in opts:
        if o in ("-t", "--type"):
            type = a
        if o in ("-h", "--help"):
            usage()
            sys.exit()

    if type == None:
            usage()
            sys.exit()
    else:
        
        if type not in types:
            om.out.information( 'Card type not found.' )
            return 2
        else:
        
            if type == 'mastercard':
                mastercard = credit_card_number(generator, mastercardPrefixList, 16, 1)
                om.out.information( output("Mastercard", mastercard) )
            
            if type == 'visa16':
                visa16 = credit_card_number(generator, visaPrefixList, 16, 1)
                om.out.information( output("VISA 16 digit", visa16) )
                
            if type == 'visa13':
                visa13 = credit_card_number(generator, visaPrefixList, 13, 1)
                om.out.information( output("VISA 13 digit", visa13) )
                
            if type == 'amex':
                amex = credit_card_number(generator, amexPrefixList, 15, 1)
                om.out.information( output("American Express", amex) )
                
                # Minor cards
            if type == 'discover':
                discover = credit_card_number(generator, discoverPrefixList, 16, 1)
                om.out.information( output("Discover", discover) )
            
            if type == 'diners':
                diners = credit_card_number(generator, dinersPrefixList, 14, 1)
                om.out.information( output("Diners Club / Carte Blanche", diners) )
            
            if type == 'enRoute':
                enRoute = credit_card_number(generator, enRoutePrefixList, 15, 1)
                om.out.information( output("enRoute", enRoute) )
                
            if type == 'jcb15':
                jcb15 = credit_card_number(generator, jcbPrefixList15, 15, 1)
                om.out.information( output("JCB 15 digit", jcb15) )
                
            if type == 'jcb16':
                jcb16 = credit_card_number(generator, jcbPrefixList16, 16, 1)
                om.out.information( output("JCB 16 digit", jcb16) )
                
            if type == 'voyager':
                voyager = credit_card_number(generator, voyagerPrefixList, 15, 1)
                om.out.information( output("Voyager", voyager) )
            
            return 0
        
if __name__ == "__main__":
  main()
  
