#!/usr/bin/env python

"""lexconvert v0.173 - convert between lexicons of different speech synthesizers
(c) 2007-2012,2014 Silas S. Brown.  License: GPL"""

# Run without arguments for usage information

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

# Old versions of this code are being kept on SourceForge's E-GuideDog SVN at
# http://svn.code.sf.net/p/e-guidedog/code/ssb22/lexconvert
# although some early ones are missing.

def Phonemes():
   """Create phonemes by calling vowel(), consonant(),
     variant() and other().
   
     For the variants, if a particular variant does not
     exist in the destination format then we will treat it
     as equivalent to the last non-variant we created.
  
     For anything else that does not exist in the
     destination format, we will first try to break the
     source's phoneme into parts (e.g. see the treatment
     of opt_ol_as_in_gold by eSpeak and bbcmicro), and if
     that still doesn't work then we drop a character
     (warning depending on the source format's setting of
     safe_to_drop_characters).  makeDic does however warn
     about any non-variant consonants, or non-variant
     vowels that weren't marked optional, missing from a
     format. """
   a_as_in_ah = vowel()
   _, var1_a_as_in_ah = variant()
   _, var2_a_as_in_ah = variant()
   _, var3_a_as_in_ah = variant()
   _, var4_a_as_in_ah = variant()
   _, var5_a_as_in_ah = variant()
   a_as_in_apple = vowel()
   u_as_in_but = vowel() # or the first part of un as in hunt
   o_as_in_orange = vowel()
   _, var1_o_as_in_orange = variant()
   _, var2_o_as_in_orange = variant()
   o_as_in_now = vowel()
   _, var1_o_as_in_now = variant()
   a_as_in_ago = vowel()
   _, var1_a_as_in_ago = variant()
   e_as_in_herd = vowel()
   eye = vowel()
   _, var1_eye = variant()
   b = consonant()
   ch = consonant()
   d = consonant()
   th_as_in_them = consonant()
   e_as_in_them = vowel()
   _, var1_e_as_in_them = variant()
   ar_as_in_year = vowel()
   a_as_in_air = vowel()
   _, var1_a_as_in_air = variant()
   _, var2_a_as_in_air = variant()
   _, var3_a_as_in_air = variant()
   _, var4_a_as_in_air = variant()
   a_as_in_ate = vowel()
   _, var1_a_as_in_ate = variant()
   f = consonant()
   g = consonant()
   h = consonant()
   i_as_in_it = vowel()
   _, var1_i_as_in_it = variant()
   _, var2_i_as_in_it = variant()
   ear = vowel()
   _, var1_ear = variant()
   _, var2_ear = variant()
   e_as_in_eat = vowel()
   _, var1_e_as_in_eat = variant()
   j_as_in_jump = consonant()
   k = consonant()
   _, opt_scottish_loch = variant()
   l = consonant()
   _, var1_l = variant()
   m = consonant()
   n = consonant()
   ng = consonant()
   o_as_in_go = vowel()
   _, var1_o_as_in_go = variant()
   _, var2_o_as_in_go = variant()
   _, var3_o_as_in_go = variant()
   opt_ol_as_in_gold = opt_vowel() # see eSpeak / bbcmicro
   oy_as_in_toy = vowel()
   _, var1_oy_as_in_toy = variant()
   p = consonant()
   r = consonant()
   _, var1_r = variant()
   s = consonant()
   sh = consonant()
   t = consonant()
   _, var1_t = variant()
   th = consonant()
   oor_as_in_poor = vowel()
   _, var1_oor_as_in_poor = variant()
   _, opt_u_as_in_pull = variant()
   opt_ul_as_in_pull = opt_vowel() # see eSpeak / bbcmicro
   oo_as_in_food = vowel()
   _, var1_oo_as_in_food = variant()
   _, var2_oo_as_in_food = variant()
   close_to_or = vowel()
   _, var1_close_to_or = variant()
   _, var2_close_to_or = variant()
   _, var3_close_to_or = variant()
   v = consonant()
   w = consonant()
   _, var1_w = variant()
   y = consonant()
   z = consonant()
   ge_of_blige_etc = consonant()
   glottal_stop = other()
   syllable_separator = other()
   _, primary_stress = variant()
   _, secondary_stress = variant()
   text_sharp = other()
   text_underline = other()
   text_question = other()
   text_exclamation = other()
   text_comma = other()
   del _ ; return locals()

def LexFormats():
  """Makes the phoneme conversion tables of each format.
     Each table has string to phoneme entries and phoneme
     to string entries.  The string to phoneme entries are
     used when converting OUT of that format, and the
     phoneme to string entries are used when converting IN
     (so you can recognise phonemes you don't support and
     convert them to something else).  By default, a tuple
     of the form (string,phoneme) will create entries in
     BOTH directions; one-directional entries are created
     via (string,phoneme,False) or (phoneme,string,False).
     The makeDic function checks the keys are unique.
     
     First parameter is always a description of the
     format, then come the phoneme entries as described
     above, then any additional settings:

       stress_comes_before_vowel (default False means any
       stress mark goes AFTER the affected vowel; set to
       True if the format requires stress placed before)
  
       space_separates_words_not_phonemes (default False
       means space is assumed to be required between each
       phoneme; True means space separates whole words)

       safe_to_drop_characters (default False, can be a
       string of safe characters or True = all; controls
       warnings when unrecognised characters are found)

       cleanup_regexps (default none) - optional list of
       (search,replace) regular expressions to "clean up"
       after converting INTO this format

       cvtOut_regexps (default none) - optional list of
       (search,replace) regular expressions to "clean up"
       before starting to convert OUT of this format
  
       inline_format (default "%s") the format string for
       printing a word with --phones or --phones2phones
       (can be used to put markup around each word)

       inline_header (default none) a line to print first
       when outputting from --phones or --phones2phones

       lex_filename - filename of a lexicon file.  If this
       is not specified, there is no support for writing a
       lexicon in this format: there can still be READ
       support if you define lex_read_function to open the
       lexicon by itself, but otherwise the format can be
       used only with --phones and --phones2phones.

       lex_entry_format - format string for writing each
       (word, pronunciation) entry to the lexicon file.
       This is also needed for lexicon-write support.

       lex_header, lex_footer - optional strings to write
       at the beginning and at the end of the lexicon file

       lex_word_case - optional "upper" or "lower" to
       force a particular case for lexicon words (not
       pronunciations - they're determined by the table).
       The default is to allow words to be in either case.

       lex_read_function - Python function to READ the
       lexicon file and return a (word,definition) list.
       If this is not specified, there's no read support
       for lexicons in this format (but there can still be
       write support - see above - and you can still use
       --phones and --phones2phones).  If lex_filename is
       specified then this function will be given the open
       file as a parameter. """
  
  phonemes = Phonemes() ; globals().update(phonemes)
  return { "festival" : makeDic(
    "Festival's British voice",
    ('0',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('aa',a_as_in_ah),
    ('a',a_as_in_apple),
    ('uh',u_as_in_but),
    ('o',o_as_in_orange),
    ('au',o_as_in_now),
    ('@',a_as_in_ago),
    ('@@',e_as_in_herd),
    ('ai',eye),
    ('b',b),
    ('ch',ch),
    ('d',d),
    ('dh',th_as_in_them),
    ('e',e_as_in_them),
    (ar_as_in_year,'@@',False),
    ('e@',a_as_in_air),
    ('ei',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('i',i_as_in_it),
    ('i@',ear),
    ('ii',e_as_in_eat),
    ('jh',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('ng',ng),
    ('ou',o_as_in_go),
    ('oi',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('sh',sh),
    ('t',t),
    ('th',th),
    ('u@',oor_as_in_poor),
    ('u',opt_u_as_in_pull),
    ('uu',oo_as_in_food),
    ('oo',close_to_or),
    ('v',v),
    ('w',w),
    ('y',y),
    ('z',z),
    ('zh',ge_of_blige_etc),
    # lex_filename etc not set (read-only for now)
    lex_read_function = lambda *args: eval('['+commands.getoutput("grep '^(lex.add.entry' ~/.festivalrc | sed -e 's/;.*//' -e 's/[^\"]*\"/[\"/' -e 's/\" . /\",(\"/' -e 's/$/\"],/' -e 's/[()]/ /g' -e 's/  */ /g'")+']'),
    safe_to_drop_characters=True, # TODO: really? (could instead give a string of known-safe characters)
  ),

  "espeak" : makeDic(
    "eSpeak's default British voice", # but eSpeak's phoneme representation isn't always that simple, hence the regexps at the end
    ('%',syllable_separator),
    ("'",primary_stress),
    (',',secondary_stress),
    # TODO: glottal_stop? (in regional pronunciations etc)
    ('A:',a_as_in_ah),
    ('A@',a_as_in_ah,False),
    ('A',var1_a_as_in_ah),
    ('a',a_as_in_apple),
    ('aa',a_as_in_apple,False),
    ('a2',a_as_in_apple,False), # TODO: this is actually an a_as_in_apple variant in espeak; festival @1 is not in mrpa PhoneSet
    ('&',a_as_in_apple,False),
    ('V',u_as_in_but),
    ('0',o_as_in_orange),
    ('aU',o_as_in_now),
    ('@',a_as_in_ago),
    ('a#',a_as_in_ago,False), # (TODO: eSpeak sometimes uses a# in 'had' when in a sentence, and this doesn't always sound good on other synths; might sometimes want to convert it to a_as_in_apple; not sure what contexts would call for this though)
    ('3:',e_as_in_herd),
    ('3',var1_a_as_in_ago),
    ('@2',a_as_in_ago,False),
    ('@-',a_as_in_ago,False), # (eSpeak @- sounds to me like a shorter version of @, TODO: double-check the relationship between @ and @2 in Festival)
    ('aI',eye),
    ('aI2',eye,False),
    ('aI;',eye,False),
    ('aI2;',eye,False),
    ('b',b),
    ('tS',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    (ar_as_in_year,'3:',False),
    ('e@',a_as_in_air),
    ('eI',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('I;',i_as_in_it,False),
    ('i',i_as_in_it,False),
    ('I2',var2_i_as_in_it,False),
    ('I2;',var2_i_as_in_it,False),
    ('i@',ear),
    ('i@3',var2_ear),
    ('i:',e_as_in_eat),
    ('i:;',e_as_in_eat,False),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('L',l,False),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('oU',o_as_in_go),
    ('oUl',opt_ol_as_in_gold), # (espeak says "gold" in a slightly 'posh' way though) (if dest format doesn't have opt_ol_as_in_gold, it'll get o_as_in_go + the l)
    ('OI',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('r-',r,False),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('@5',opt_u_as_in_pull,False),
    ('Ul',opt_ul_as_in_pull), # if dest format doesn't have this, it'll get opt_u_as_in_pull from the U, then the l
    ('u:',oo_as_in_food),
    ('O:',close_to_or),
    ('O@',var3_close_to_or),
    ('o@',var3_close_to_or,False),
    ('O',var3_close_to_or,False),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename = "en_extra",
    lex_entry_format = "%s %s\n",
    lex_read_function = lambda lexfile: [x for x in [l.split()[:2] for l in lexfile.readlines()] if len(x)==2 and not '//' in x[0]],
    inline_format = "[[%s]]",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters="_: !",
    cleanup_regexps=[
      ("k'a2n","k'@n"),
      ("ka2n","k@n"),
      ("gg","g"),
      ("@U","oU"), # (eSpeak uses oU to represent @U; difference is given by its accent parameters)
      ("([iU]|([AO]:))@r$","\1@"),
      ("([^e])@r",r"\1_remove_3"),("_remove_",""),
      # (r"([^iU]@)l",r"\1L") # only in older versions of espeak (not valid in more recent versions)
      ("rr$","r"),
      ("3:r$","3:"),
      # TODO: 'declared' & 'declare' the 'r' after the 'E' sounds a bit 'regional' (but pretty).  but sounds incomplete w/out 'r', and there doesn't seem to be an E2 or E@
      # TODO: consider adding 'g' to words ending in 'N' (if want the 'g' pronounced in '-ng' words) (however, careful of words like 'yankee' where the 'g' would be followed by a 'k'; this may also be a problem going into the next word)
    ],
     cvtOut_regexps = [
       ("e@r$","e@"), ("e@r([bdDfghklmnNprsStTvwjzZ])",r"e@\1"), # because the 'r' is implicit in other synths (but DO have it if there's another vowel to follow)
     ],
  ),

  "sapi" : makeDic(
    "Microsoft Speech API (American English)",
    ('-',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('aa',a_as_in_ah),
    ('ae',a_as_in_apple),
    ('ah',u_as_in_but),
    ('ao',o_as_in_orange),
    ('aw',o_as_in_now),
    ('ax',a_as_in_ago),
    ('er',e_as_in_herd),
    ('ay',eye),
    ('b',b),
    ('ch',ch),
    ('d',d),
    ('dh',th_as_in_them),
    ('eh',e_as_in_them),
    ('ey',var1_e_as_in_them),
    (ar_as_in_year,'er',False),
    ('eh r',a_as_in_air),
    (a_as_in_ate,'ey',False),
    ('f',f),
    ('g',g),
    ('h',h), # Jan suggested 'hh', but I can't get this to work on Windows XP (TODO: try newer versions of Windows)
    ('ih',i_as_in_it),
    ('iy ah',ear),
    ('iy',e_as_in_eat),
    ('jh',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('ng',ng),
    ('ow',o_as_in_go),
    ('oy',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('sh',sh),
    ('t',t),
    ('th',th),
    ('uh',oor_as_in_poor),
    ('uw',oo_as_in_food),
    ('AO',close_to_or),
    ('v',v),
    ('w',w),
    # ('x',var1_w), # suggested by Jan, but I can't get this to work on Windows XP (TODO: try newer versions of Windows)
    ('y',y),
    ('z',z),
    ('zh',ge_of_blige_etc),
    lex_filename="run-ptts.bat", # write-only for now
    lex_header = "rem  You have to run this file\nrem  with ptts.exe in the same directory\nrem  to add these words to the SAPI lexicon\n\n",
    lex_entry_format='ptts -la %s "%s"\n',
    inline_format = '<pron sym="%s"/>',
    safe_to_drop_characters=True, # TODO: really?
  ),

  "cepstral" : makeDic(
    "Cepstral's British English SSML phoneset",
    ('0',syllable_separator),
    ('1',primary_stress),
    ('a',a_as_in_ah),
    ('ae',a_as_in_apple),
    ('ah',u_as_in_but),
    ('oa',o_as_in_orange),
    ('aw',o_as_in_now),
    (a_as_in_ago,'ah',False),
    ('er',e_as_in_herd),
    ('ay',eye),
    ('b',b),
    ('ch',ch),
    ('d',d),
    ('dh',th_as_in_them),
    ('eh',e_as_in_them),
    (ar_as_in_year,'er',False),
    ('e@',a_as_in_air),
    ('ey',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('ih',i_as_in_it),
    ('i ah',ear),
    ('i',e_as_in_eat),
    ('jh',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('ng',ng),
    ('ow',o_as_in_go),
    ('oy',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('sh',sh),
    ('t',t),
    ('th',th),
    ('uh',oor_as_in_poor),
    ('uw',oo_as_in_food),
    ('ao',close_to_or),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('zh',ge_of_blige_etc),
    lex_filename="lexicon.txt",
    lex_entry_format = "%s 0 %s\n",
    lex_read_function = lambda lexfile: [(word,pronunc) for word, ignore, pronunc in [l.split(None,2) for l in lexfile.readlines()]],
    lex_word_case = "lower",
    inline_format = "<phoneme ph='%s'>p</phoneme>",
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[(" 1","1"),(" 0","0")],
  ),

  "mac" : makeDic(
    "approximation in American English using the [[inpt PHON]] notation of Apple's US voices",
    ('=',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('AA',a_as_in_ah),
    ('aa',var5_a_as_in_ah),
    ('AE',a_as_in_apple),
    ('UX',u_as_in_but),
    (o_as_in_orange,'AA',False),
    ('AW',o_as_in_now),
    ('AX',a_as_in_ago),
    (e_as_in_herd,'AX',False), # TODO: is this really the best approximation?
    ('AY',eye),
    ('b',b),
    ('C',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('EH',e_as_in_them),
    (ar_as_in_year,'AX',False),
    ('EH r',a_as_in_air),
    ('EY',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('IH',i_as_in_it),
    ('IX',var2_i_as_in_it),
    ('IY UX',ear),
    ('IY',e_as_in_eat),
    ('J',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('OW',o_as_in_go),
    ('OY',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('UH',oor_as_in_poor),
    ('UW',oo_as_in_food),
    ('AO',close_to_or),
    ('v',v),
    ('w',w),
    ('y',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename="substitute.sh", # write-only for now
    lex_header = "# I don't yet know how to add to the Apple US lexicon,\n# so here is a 'sed' command you can run on your text\n# to put the pronunciation inline:\n\nsed",
    lex_entry_format=' -e "s/%s/[[inpt PHON]]%s[[inpt TEXT]]/g"',
    lex_footer = "\n",
    inline_format = "[[inpt PHON]]%s[[inpt TEXT]]",
    space_separates_words_not_phonemes=True,
    safe_to_drop_characters=True, # TODO: really?
  ),

  "mac-uk" : makeDic(
    "Scansoft/Nuance British voices for Mac OS 10.7+ (system lexicon editing required, see --mac-uk option)",
    ('.',syllable_separator),
    ("'",primary_stress),
    ('',secondary_stress),
    ('A',a_as_in_ah),
    ('@',a_as_in_apple),
    ('$',u_as_in_but),
    (a_as_in_ago,'$',False),
    ('A+',o_as_in_orange),
    ('a&U',o_as_in_now),
    ('E0',e_as_in_herd),
    ('a&I',eye),
    ('b',b),
    ('t&S',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    ('0',ar_as_in_year),
    ('E&$',a_as_in_air),
    ('e&I',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    (ear,'E0',False),
    ('i',e_as_in_eat),
    ('d&Z',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('nK',ng),
    ('o&U',o_as_in_go),
    ('O&I',oy_as_in_toy),
    ('p',p),
    ('R+',r),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('O',oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    (oo_as_in_food,'U',False),
    (close_to_or,'O',False),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    # lex_filename not set (mac-uk code does not permanently save the lexicon; see --mac-uk option to read text)
    inline_header = "mac-uk phonemes output is for information only; you'll need the --mac-uk or --trymac-uk options to use it\n",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[(r'o\&U\.Ol', r'o\&Ul')],
  ),

  "x-sampa" : makeDic(
    "General X-SAMPA notation (contributed by Jan Weiss)",
    ('.',syllable_separator),
    ('"',primary_stress),
    ('%',secondary_stress),
    ('A',a_as_in_ah),
    (':',var2_a_as_in_ah),
    ('A:',var3_a_as_in_ah),
    ('Ar\\',var4_a_as_in_ah),
    ('a:',var5_a_as_in_ah),
    ('{',a_as_in_apple),
    ('V',u_as_in_but),
    ('Q',o_as_in_orange),
    (var1_o_as_in_orange,'A',False),
    ('O',var2_o_as_in_orange),
    ('aU',o_as_in_now),
    ('{O',var1_o_as_in_now),
    ('@',a_as_in_ago),
    ('3:',e_as_in_herd),
    ('aI',eye),
    ('Ae',var1_eye),
    ('b',b),
    ('tS',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    ('e',var1_e_as_in_them),
    (ar_as_in_year,'3:',False),
    ('E@',a_as_in_air),
    ('Er\\',var1_a_as_in_air),
    ('e:',var2_a_as_in_air),
    ('E:',var3_a_as_in_air),
    ('e@',var4_a_as_in_air),
    ('eI',a_as_in_ate),
    ('{I',var1_a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('1',var1_i_as_in_it),
    ('I@',ear),
    ('Ir\\',var1_ear),
    ('i',e_as_in_eat),
    ('i:',var1_e_as_in_eat),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('@U',o_as_in_go),
    ('oU',var2_o_as_in_go),
    ('@}',var3_o_as_in_go),
    ('OI',oy_as_in_toy),
    ('oI',var1_oy_as_in_toy),
    ('p',p),
    ('r\\',r),
    (var1_r,'r',False),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('Ur\\',var1_oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('}:',oo_as_in_food),
    ('u:',var1_oo_as_in_food),
    (var2_oo_as_in_food,'u:',False),
    ('O:',close_to_or),
    (var1_close_to_or,'O',False),
    ('o:',var2_close_to_or),
    ('v',v),
    ('w',w),
    ('W',var1_w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename="acapela.txt",
    lex_entry_format = "%s\t#%s\tUNKNOWN\n", # TODO: may be able to convert part-of-speech (NOUN etc) to/from some other formats e.g. Festival
    lex_read_function=lambda lexfile:[(word,pronunc.lstrip("#")) for word, pronunc, ignore in [l.split(None,2) for l in lexfile.readlines()]],
    # TODO: inline_format ?
    space_separates_words_not_phonemes=True,
    safe_to_drop_characters=True, # TODO: really?
  ),

  "acapela-uk" : makeDic(
    'Acapela-optimised X-SAMPA for UK English voices (e.g. "Peter"), contributed by Jan Weiss',
    ('A:',a_as_in_ah),
    ('{',a_as_in_apple),
    ('V',u_as_in_but),
    ('Q',o_as_in_orange),
    ('A',var1_o_as_in_orange),
    ('O',var2_o_as_in_orange),
    ('aU',o_as_in_now),
    ('{O',var1_o_as_in_now),
    ('@',a_as_in_ago),
    ('3:',e_as_in_herd),
    ('aI',eye),
    ('A e',var1_eye),
    ('b',b),
    ('t S',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('e',e_as_in_them),
    (ar_as_in_year,'3:',False),
    ('e @',a_as_in_air),
    ('e r',var1_a_as_in_air),
    ('e :',var2_a_as_in_air),
    (var3_a_as_in_air,'e :',False),
    ('eI',a_as_in_ate),
    ('{I',var1_a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('1',var1_i_as_in_it),
    ('I@',ear),
    ('I r',var1_ear),
    ('i',e_as_in_eat),
    ('i:',var1_e_as_in_eat),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('@U',o_as_in_go),
    ('o U',var2_o_as_in_go),
    ('@ }',var3_o_as_in_go),
    ('OI',oy_as_in_toy),
    ('o I',var1_oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('U r',var1_oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('u:',oo_as_in_food),
    ('O:',close_to_or),
    (var1_close_to_or,'O',False),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename="acapela.txt",
    lex_entry_format = "%s\t#%s\tUNKNOWN\n", # TODO: part-of-speech (as above)
    lex_read_function=lambda lexfile:[(word,pronunc.lstrip("#")) for word, pronunc, ignore in [l.split(None,2) for l in lexfile.readlines()]],
    inline_format = "\\Prn=%s\\",
    safe_to_drop_characters=True, # TODO: really?
  ),

  "cmu" : makeDic(
    'format of the US-English Carnegie Mellon University Pronouncing Dictionary (contributed by Jan Weiss)', # http://www.speech.cs.cmu.edu/cgi-bin/cmudict
    ('0',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('AA',a_as_in_ah),
    (var1_a_as_in_ah,'2',False),
    (var2_a_as_in_ah,'1',False),
    ('AE',a_as_in_apple),
    ('AH',u_as_in_but),
    (o_as_in_orange,'AA',False),
    ('AW',o_as_in_now),
    (a_as_in_ago,'AH',False),
    ('ER',e_as_in_herd), # TODO: check this one
    ('AY',eye),
    ('B ',b),
    ('CH',ch),
    ('D ',d),
    ('DH',th_as_in_them),
    ('EH',e_as_in_them),
    (ar_as_in_year,'ER',False),
    (a_as_in_air,'ER',False),
    ('EY',a_as_in_ate),
    ('F ',f),
    ('G ',g),
    ('HH',h),
    ('IH',i_as_in_it),
    ('EY AH',ear),
    ('IY',e_as_in_eat),
    ('JH',j_as_in_jump),
    ('K ',k),
    ('L ',l),
    ('M ',m),
    ('N ',n),
    ('NG',ng),
    ('OW',o_as_in_go),
    ('OY',oy_as_in_toy),
    ('P ',p),
    ('R ',r),
    ('S ',s),
    ('SH',sh),
    ('T ',t),
    ('TH',th),
    ('UH',oor_as_in_poor),
    ('UW',oo_as_in_food),
    ('AO',close_to_or),
    ('V ',v),
    ('W ',w),
    ('Y ',y),
    ('Z ',z),
    ('ZH',ge_of_blige_etc),
    # lex_filename not set (does CMU have a lex file?)
    safe_to_drop_characters=True, # TODO: really?
  ),

  "bbcmicro" : makeDic(
    "BBC Micro Speech program from 1985 (see comments in lexconvert.py for more details)",
    # Speech was written by David J. Hoskins and published by Superior Software.  It took 7.5k of RAM including 3.1k of samples (49 phonemes + 1 for fricatives at 64 bytes each, 4-bit ~5.5kHz), 2.2k of lexicon, and 2.2k of machine code; sounds "retro" by modern standards but quite impressive for the BBC Micro in 1985.  Samples are played by amplitude-modulating the BBC's tone generator.
    # If you use an emulator like BeebEm, you'll need diskimg/Speech.ssd.  This can be made from your original Speech disc, or you might be able to find one but beware of copyright!  Same goes with the Model B ROM images included in BeebEm (you might want to delete the other models).  There has been considerable discussion over whether UK copyright law does or should allow "format-shifting" your own legally-purchased media, and I don't fully understand all the discussion so I don't want to give advice on it here.  The issue is "format-shifting" your legally-purchased BBC Micro ROM code and Speech disc to emulator images; IF this is all right then I suspect downloading someone else's copy is arguably allowed as long as you bought it legally "back in the day", but I'm not a solicitor so I don't know.
    # lexconvert's --phones bbcmicro option creates *SPEAK commands which you can type into the BBC Micro or paste into an emulator, either at the BASIC prompt, or in a listing with line numbers provided by AUTO.  You have to load the Speech program first of course.
    # To script this on BeebEm, first turn off the Speech disc's boot option (by turning off File / Disc options / Write protect and entering "*OPT 4,0"; use "*OPT 4,3" if you want it back later; if you prefer to edit the disk image outside of the emulator then change byte 0x106 from 0x33 to 0x03), and then you can do (e.g. on a Mac) open /usr/local/BeebEm3/diskimg/Speech.ssd && sleep 1 && (echo '*SPEECH';python lexconvert.py --phones bbcmicro "Greetings from 19 85") | pbcopy && osascript -e 'tell application "System Events" to keystroke "v" using command down'
    # or if you know it's already loaded: echo "Here is some text" | python lexconvert.py --phones bbcmicro | pbcopy && osascript -e 'tell application "BeebEm3" to activate' && osascript -e 'tell application "System Events" to keystroke "v" using command down'
    # (unfortunately there doesn't seem to be a way of doing it without giving the emulator window focus)
    # If you want to emulate a Master, you might need a *DISK before the *SPEECH (to take it out of ADFS mode)
    ('4',primary_stress),
    ('5',secondary_stress), # (these are pitch numbers on the BBC; normal pitch is 6, and lower numbers are higher pitches, so try 5=secondary and 4=primary; 3 sounds less calm)
    ('AA',a_as_in_ah),
    ('AE',a_as_in_apple),
    ('AH',u_as_in_but),
    ('O',o_as_in_orange),
    ('AW',o_as_in_now),
    (a_as_in_ago,'AH',False),
    ('ER',e_as_in_herd),
    ('IY',eye),
    ('B',b),
    ('CH',ch),
    ('D',d),
    ('DH',th_as_in_them),
    ('EH',e_as_in_them),
    (ar_as_in_year,'ER',False),
    ('AI',a_as_in_air),
    ('AY',a_as_in_ate),
    ('F',f),
    ('G',g),
    ('/H',h),
    ('IH',i_as_in_it),
    ('IX',var2_i_as_in_it), # (IX sounds to me like a slightly shorter version of IH)
    ('IXAH',ear),
    ('EER',var2_ear), # e.g. 'hear', 'near' - near enough
    ('EE',e_as_in_eat),
    ('J',j_as_in_jump),
    ('K',k),
    ('C',k,False), # for CT as in "fact", read out as K+T
    ('L',l),
    ('M',m),
    ('N',n),
    ('NX',ng),
    ('OW',o_as_in_go),
    ('OL',opt_ol_as_in_gold), # (if dest format doesn't have this, it'll get o_as_in_orange from the O, then the l)
    ('OY',oy_as_in_toy),
    ('P',p),
    ('R',r),
    ('S',s),
    ('SH',sh),
    ('T',t),
    ('TH',th),
    ('AOR',oor_as_in_poor),
    ('UH',oor_as_in_poor,False), # TODO: really? (espeak 'U' goes to opt_u_as_in_pull, and eSpeak also used U for the o in good, which sounds best with Speech's default UH4, hence the line below, but where did we get UH->oor_as_in_poor from?  Low-priority though because how often do you convert OUT of bbcmicro format)
    (opt_u_as_in_pull,'UH',False),
    ('/U',opt_u_as_in_pull,False),
    ('/UL',opt_ul_as_in_pull), # if dest format doesn't have this, it'll get opt_u_as_in_pull from the /U, then l
    ('UW',oo_as_in_food),
    ('UX',oo_as_in_food,False),
    ('AO',close_to_or),
    ('V',v),
    ('W',w),
    ('Y',y),
    ('Z',z),
    ('ZH',ge_of_blige_etc),
    lex_filename=ifset("MAKE_SPEECH_ROM","SPEECH.ROM","BBCLEX"),
    lex_entry_format="> %s_"+chr(128)+"%s", # (specifying 'whole word' for now; remove the space before or the _ after if you want)
    lex_read_function = lambda lexfile: [(w[0].lstrip().rstrip('_').lower(),w[1]) for w in filter(lambda x:len(x)==2,[w.split(chr(128)) for w in lexfile.read().split('>')])], # TODO: this reads back the entries we generate, but is unlikely to work well with the wildcards in the default lexicon that would have been added if SPEECH_DISK was set (c.f. trying to read eSpeak's en_rules instead of en_extra)
    lex_word_case = "upper",
    lex_footer = ">**",
    # inline_format not set - handled by special-case code
    space_separates_words_not_phonemes=True,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[
      ('KT','CT'), # Speech instructions: "CT as in fact"
      ('DYUW','DUX'), # "DUX as in duke"
      ('AHR$','AH'), # usually sounds a bit better
    ],
    cvtOut_regexps=[('DUX','DYUW')], # CT handled above
  ),

  "unicode-ipa" : makeDic(
    "Unicode IPA (as used in an increasing number of dictionary programs, websites etc)",
    ('.',syllable_separator,False),
    (u'\u02c8',primary_stress),
    (u'\u02cc',secondary_stress),
    ('#',text_sharp),
    ('_',text_underline),
    ('?',text_question),
    ('!',text_exclamation),
    (',',text_comma),
    (u'\u0251',a_as_in_ah),
    (u'\u02d0',var2_a_as_in_ah),
    (u'\u0251\u02d0',var3_a_as_in_ah),
    (u'\u0251\u0279',var4_a_as_in_ah),
    ('a\\u02d0',var5_a_as_in_ah),
    (u'\xe6',a_as_in_apple),
    ('a',a_as_in_apple,False),
    (u'\u028c',u_as_in_but),
    (u'\u0252',o_as_in_orange),
    (var1_o_as_in_orange,u'\u0251',False),
    (u'\u0254',var2_o_as_in_orange),
    (u'a\u028a',o_as_in_now),
    (u'\xe6\u0254',var1_o_as_in_now),
    (u'\u0259',a_as_in_ago),
    (u'\u0259\u02d0',e_as_in_herd),
    (u'\u025a',var1_a_as_in_ago),
    (u'a\u026a',eye),
    (u'\u0251e',var1_eye),
    ('b',b),
    (u't\u0283',ch),
    (u'\u02a7',ch,False),
    ('d',d),
    (u'\xf0',th_as_in_them),
    (u'\u025b',e_as_in_them),
    ('e',var1_e_as_in_them),
    (u'\u025d',ar_as_in_year),
    (u'\u025c\u02d0',ar_as_in_year,False),
    (u'\u025b\u0259',a_as_in_air),
    (u'\u025b\u0279',var1_a_as_in_air),
    (u'e\u02d0',var2_a_as_in_air),
    (u'\u025b\u02d0',var3_a_as_in_air),
    (u'e\u0259',var4_a_as_in_air),
    (u'e\u026a',a_as_in_ate),
    (u'\xe6\u026a',var1_a_as_in_ate),
    ('f',f),
    (u'\u0261',g),
    ('h',h),
    (u'\u026a',i_as_in_it),
    (u'\u0268',var1_i_as_in_it),
    (u'\u026a\u0259',ear),
    (u'\u026a\u0279',var1_ear),
    (u'\u026a\u0279\u0259',var2_ear), # ?
    ('i',e_as_in_eat),
    (u'i\u02d0',var1_e_as_in_eat),
    (u'd\u0292',j_as_in_jump),
    (u'\u02a4',j_as_in_jump,False),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    (u'd\u026b',var1_l),
    ('m',m),
    ('n',n),
    (u'\u014b',ng),
    (u'\u0259\u028a',o_as_in_go),
    ('o',var1_o_as_in_go),
    (u'o\u028a',var2_o_as_in_go),
    (u'\u0259\u0289',var3_o_as_in_go),
    (u'\u0254\u026a',oy_as_in_toy),
    (u'o\u026a',var1_oy_as_in_toy),
    ('p',p),
    (u'\u0279',r),
    (var1_r,'r',False),
    ('s',s),
    (u'\u0283',sh),
    ('t',t),
    (u'\u027e',var1_t),
    (u'\u03b8',th),
    (u'\u028a\u0259',oor_as_in_poor),
    (u'\u028a\u0279',var1_oor_as_in_poor),
    (u'\u028a',opt_u_as_in_pull),
    (u'\u0289\u02d0',oo_as_in_food),
    (u'u\u02d0',var1_oo_as_in_food),
    ('u',var2_oo_as_in_food),
    (u'\u0254\u02d0',close_to_or),
    (var1_close_to_or,u'\u0254',False),
    (u'o\u02d0',var2_close_to_or),
    ('v',v),
    ('w',w),
    (u'\u028d',var1_w),
    ('j',y),
    ('z',z),
    (u'\u0292',ge_of_blige_etc),
    (u'\u0294',glottal_stop),
    lex_filename="words-ipa.html", # write-only for now
    lex_header = '<html><head><meta name="mobileoptimized" content="0"><meta name="viewport" content="width=device-width"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><table>',
    lex_entry_format="<tr><td>%s</td><td>%s</td></tr>\n",
    lex_footer = "</table></body></html>\n",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters=True, # TODO: really? (at least '-' should be safe to drop)
  ),

  "latex-ipa" : makeDic(
    "LaTeX IPA package (in case you need to typeset your custom pronunciations in an academic paper or something)",
    ('.',syllable_separator,False),
    ('"',primary_stress),
    ('\\textsecstress{}',secondary_stress),
    ('\\#',text_sharp),
    ('\\_',text_underline),
    ('?',text_question),
    ('!',text_exclamation),
    (',',text_comma),
    ('A',a_as_in_ah),
    (':',var2_a_as_in_ah),
    ('A:',var3_a_as_in_ah),
    ('A\\textturnr{}',var4_a_as_in_ah),
    ('a:',var5_a_as_in_ah),
    ('\\ae{}',a_as_in_apple),
    ('2',u_as_in_but),
    ('6',o_as_in_orange),
    (var1_o_as_in_orange,'A',False),
    ('O',var2_o_as_in_orange),
    ('aU',o_as_in_now),
    ('\\ae{}O',var1_o_as_in_now),
    ('@',a_as_in_ago),
    ('@:',e_as_in_herd),
    ('\\textrhookschwa{}',var1_a_as_in_ago),
    ('aI',eye),
    ('Ae',var1_eye),
    ('b',b),
    ('tS',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    ('e',var1_e_as_in_them),
    ('3:',ar_as_in_year),
    ('E@',a_as_in_air),
    ('E\\textturnr{}',var1_a_as_in_air),
    ('e:',var2_a_as_in_air),
    ('E:',var3_a_as_in_air),
    ('e@',var4_a_as_in_air),
    ('eI',a_as_in_ate),
    ('\\ae{}I',var1_a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('1',var1_i_as_in_it),
    ('I@',ear),
    ('I\\textturnr{}',var1_ear),
    ('I@\\textturnr{}',var2_ear), # ?
    ('i',e_as_in_eat),
    ('i:',var1_e_as_in_eat),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('d\\textltilde{}',var1_l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('@U',o_as_in_go),
    ('o',var1_o_as_in_go),
    ('oU',var2_o_as_in_go),
    ('@0',var3_o_as_in_go),
    ('OI',oy_as_in_toy),
    ('oI',var1_oy_as_in_toy),
    ('p',p),
    ('\\textturnr{}',r),
    (var1_r,'r',False),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('R',var1_t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('U\\textturnr{}',var1_oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('0:',oo_as_in_food),
    ('u:',var1_oo_as_in_food),
    ('u',var2_oo_as_in_food),
    ('O:',close_to_or),
    (var1_close_to_or,'O',False),
    ('o:',var2_close_to_or),
    ('v',v),
    ('w',w),
    ('\\textturnw{}',var1_w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    ('P',glottal_stop),
    lex_filename="words-ipa.tex", # write-only for now
    lex_header = r'\documentclass[12pt,a4paper]{article} \usepackage[safe]{tipa} \usepackage{longtable} \begin{document} \begin{longtable}{ll}',
    lex_entry_format=r"%s & \textipa{%s}\\"+"\n",
    lex_footer = r"\end{longtable}\end{document}"+"\n",
    inline_format = "\\textipa{%s}",
    inline_header = r"% In preamble, put \usepackage[safe]{tipa}", # (the [safe] part is recommended if you're mixing with other TeX)
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters=True, # TODO: really?
  ),

  "pinyin-approx" : makeDic(
    "Rough approximation using roughly the spelling rules of Chinese Pinyin (for getting Chinese-only voices to speak some English words - works with some words better than others)", # write-only for now
    ('4',primary_stress),
    ('2',secondary_stress),
    ('a5',a_as_in_ah),
    ('ya5',a_as_in_apple),
    ('e5',u_as_in_but),
    ('yo5',o_as_in_orange),
    ('ao5',o_as_in_now),
    (a_as_in_ago,'e5',False),
    (e_as_in_herd,'e5',False),
    ('ai5',eye),
    ('bu0',b),
    ('che0',ch),
    ('de0',d),
    ('ze0',th_as_in_them),
    ('ye5',e_as_in_them),
    (ar_as_in_year,'e5',False),
    (a_as_in_air,'ye5',False),
    ('ei5',a_as_in_ate),
    ('fu0',f),
    ('ge0',g),
    ('he0',h),
    ('yi5',i_as_in_it),
    ('yi3re5',ear),
    (e_as_in_eat,'yi5',False),
    ('zhe0',j_as_in_jump),
    ('ke0',k),
    ('le0',l),
    ('me0',m),
    ('ne0',n),
    ('eng0',ng),
    ('ou5',o_as_in_go),
    ('ruo2yi5',oy_as_in_toy),
    ('pu0',p),
    ('re0',r),
    ('se0',s),
    ('she0',sh),
    ('te0',t),
    (th,'zhe0',False),
    (oor_as_in_poor,'wu5',False),
    ('yu5',oo_as_in_food),
    ('huo5',close_to_or),
    (v,'fu0',False),
    ('wu0',w),
    ('yu0',y),
    (z,'ze0',False),
    (ge_of_blige_etc,'zhe0',False),
    lex_filename="words-pinyin-approx.txt", # write-only for now
    lex_header = "Pinyin approxmations (very approximate!)\n----------------------------------------\n",
    lex_entry_format = "%s ~= %s\n",
    space_separates_words_not_phonemes=True,
    cleanup_regexps=[
      ("te0ye","tie"),
      ("e0e5","e5"),("([^aeiou][uo])0e(5)",r"\1\2"),
      ("yu0y","y"),
      ("wu0yo5","wo5"),
      ("([bdfghklmnpwz])[euo]0ei",r"\1ei"),
      ("([bdghklmnpstwz])[euo]0ai",r"\1ai"),
      ("([ghklmnpstyz])[euo]0ya",r"\1a"),("([ghklmnpstz])a([0-5]*)ne0",r"\1an\2"),
      ("([bdfghklmnpstwyz])[euo]0a([1-5])",r"\1a\2"),
      ("([bdjlmnpt])[euo]0yi",r"\1i"),("([bjlmnp])i([1-5]*)ne0",r"\1in\2"),
      ("([zs])he0ei",r"\1hei"),
      ("([dfghklmnprstyz])[euo]0ou",r"\1ou"),
      ("([dghklnrst])[euo]0huo",r"\1uo"),
      ("([bfpm])[euo]0huo",r"\1o"),
      ("([bdghklmnprstyz])[euo]0ao",r"\1ao"),
      ("([zcs])h[eu]0ao",r"\1hao"),
      ("re0r","r"),
      ("zhe0ne0","zhun5"),
      ("54","4"),
      ("52","2"),
      ("([bdjlmnpty])i([1-9])eng0",r"\1ing\2"),
      ("ya([1-9])eng0",r"yang\1"),
      ("ya([1-9])ne0",r"an\1"),
      ("ye([1-9])ne0",r"yan\1"),("([wr])[eu]0yan",r"\1en"),
      ("yi([1-9])ne0",r"yin\1"),
      
      ("yu0","yu5"),("eng0","eng5"), # they won't work unvoiced anyway
      ("0","5"), # comment out if the synth supports 'tone 0 for unvoiced'
      #("[euo]0","0"), # comment in if it expects consonants only when doing that
    ],
  ),

  "kana-approx" : makeDic(
    "Rough approximation using kana (for getting Japanese computer voices to speak some English words - works with some words better than others).  Set KANA_TYPE environment variable to hiragana or katakana (which can affect the sounds of some voices); default is hiragana", # for example try feeding it to 'say -v Kyoko' on Mac OS 10.7+ (with Japanese voice installed in System Preferences) (this voice has a built-in converter from English as well, but lexconvert --phones kana-approx can work better).  Default is hiragana because I find hiragana easier to read than katakana.  Mac OS 10.7+'s Korean voices (Yuna and Narae) can also read kana, and you could try doing a makeVariantDic and adding in some Korean jamo letters for them (you'd be pushed to represent everything in jamo but kana+jamo seems more hopeful in theory), but again some words work better than others (not all phonetic combinations are supported and some words aren't clear at all).
    # This kana-approx format is 'write-only' for now (see comment in cleanup_regexps re possible reversal)
    (u'double-',primary_stress),
    (secondary_stress,ifset('KANA_MORE_EMPH',u'double-'),False), # set KANA_MORE_EMPH environment variable if you want to try doubling the secondary-stressed vowels as well (doesn't always work very well; if it did, I'd put this line in a makeVariantDic called kana-approx-moreEmph or something)
    # The following Unicode codepoints are hiragana; KANA_TYPE is handled by some special-case code at the end of convert()
    (u'\u3042',a_as_in_apple),
    (u'\u3044',e_as_in_eat),
    (u'\u3046',oo_as_in_food),
    (u'\u3048',e_as_in_them),
    (u'\u304a',o_as_in_orange),
    (u'\u3042\u3044',eye), # ai
    (u'\u3042\u304a',o_as_in_now), # ao
    (u'\u3048\u3044',a_as_in_ate), # ei
    (u'\u304a\u3044',oy_as_in_toy), # oi
    (u'\u304a\u3046',o_as_in_go), # ou
    (a_as_in_ah,u'\u3042',False),
    (a_as_in_ago,u'\u3042',False), # TODO: really?
    (e_as_in_herd,u'\u3042',False), # TODO: really?
    (i_as_in_it,u'\u3044',False), # TODO: really?
    (u_as_in_but,u'\u3046',False), # TODO: really?
    (ar_as_in_year,u'\u3048',False), # TODO: really?
    (a_as_in_air,u'\u3048',False), # TODO: really?
    (ear,u'\u3044\u304a',False), # TODO: really?
    (oor_as_in_poor,u'\u304a',False), # TODO: really?
    (close_to_or,u'\u304a\u30fc'), # TODO: really?
    (u'\u3076',b), # bu (with vowel replacements later)
    (u'\u3061\u3047',ch), # chu (ditto)
    (u'\u3065',d), # du (and so on)
    (u'\u3066\u3085',th), (th_as_in_them,u'\u3066\u3085',False),
    (u'\u3075',f),
    (u'\u3050',g),
    (u'\u306f',h), # ha (as hu == fu)
    (u'\u3058\u3085',j_as_in_jump), (ge_of_blige_etc,u'\u3058\u3085',False),
    (u'\u304f',k),
    (u'\u308b',l), (r,u'\u308b',False),
    (u'\u3080',m),
    (u'\u306c',n),
    (u'\u3093\u3050',ng),
    (u'\u3077',p),
    (u'\u3059',s),
    (u'\u3057\u3085',sh),
    (u'\u3064',t),
    (u'\u3094',v), # TODO: is vu always supported? (it doesn't seem to show up in all fonts)
    (u'\u308f',w), # use 'wa' (as 'wu' == 'u')
    (u'\u3086',y),
    (u'\u305a',z),
    lex_filename="words-kana-approx.txt", # write-only for now
    lex_header = "Kana approxmations (very approximate!)\n--------------------------------------\n",
    lex_entry_format = "%s ~= %s\n",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    cleanup_regexps=[
       (u'double-(.)',ur'\1\u30fc'),
       (u"\u306c$",u"\u3093\u30fc"), # TODO: or u"\u3093\u3093" ?
       # now the vowel replacements (bu+a -> ba, etc) (in most cases these can be reversed into cvtOut_regexps if you want to use the kana-approx table to convert hiragana into approximate English phonemes (plus add a (u"\u3093\u30fc*",u"\u306c") and perhaps de-doubling rules to convert back to emphasis) but the result is unlikely to be any good)
       (u"\u3076\u3042",u"\u3070"),(u"\u3076\u3044",u"\u3073"),(u"\u3076\u3046",u"\u3076"),(u"\u3076\u3048",u"\u3079"),(u"\u3076\u304a",u"\u307c"),
       (u"\u3061\u3085\u3042",u"\u3061\u3083"),(u"\u3061\u3085\u3044",u"\u3061"),(u"\u3061\u3085\u3046",u"\u3061\u3085"),(u"\u3061\u3085\u3048",u"\u3061\u3047"),(u"\u3061\u3085\u304a",u"\u3061\u3087"),
       (u"\u3065\u3042",u"\u3060"),(u"\u3065\u3044",u"\u3062"),(u"\u3065\u3046",u"\u3065"),(u"\u3065\u3048",u"\u3067"),(u"\u3065\u304a",u"\u3069"),
       (u"\u3066\u3085\u3042",u"\u3066\u3083"),(u"\u3066\u3085\u3044",u"\u3066\u3043"),(u"\u3066\u3043\u3046",u"\u3066\u3085"),(u"\u3066\u3085\u3048",u"\u3066\u3047"),(u"\u3066\u3085\u304a",u"\u3066\u3087"),
       (u"\u3075\u3042",u"\u3075\u3041"),(u"\u3075\u3044",u"\u3075\u3043"),(u"\u3075\u3046",u"\u3075"),(u"\u3075\u3048",u"\u3075\u3047"),(u"\u3075\u304a",u"\u3075\u3049"),
       (u"\u306f\u3042",u"\u306f"),(u"\u306f\u3044",u"\u3072"),(u"\u306f\u3046",u"\u3075"),(u"\u306f\u3048",u"\u3078"),(u"\u306f\u304a",u"\u307b"),
       (u"\u3050\u3042",u"\u304c"),(u"\u3050\u3044",u"\u304e"),(u"\u3050\u3046",u"\u3050"),(u"\u3050\u3048",u"\u3052"),(u"\u3050\u304a",u"\u3054"),
       (u"\u3058\u3085\u3042",u"\u3058\u3083"),(u"\u3058\u3085\u304a",u"\u3058"),(u"\u3058\u3085\u3046",u"\u3058\u3085"),(u"\u3058\u3085\u3048",u"\u3058\u3047"),(u"\u3058\u3085\u304a",u"\u3058\u3087"),
       (u"\u304f\u3042",u"\u304b"),(u"\u304f\u3044",u"\u304d"),(u"\u304f\u3046",u"\u304f"),(u"\u304f\u3048",u"\u3051"),(u"\u304f\u304a",u"\u3053"),
       (u"\u308b\u3042",u"\u3089"),(u"\u308b\u3044",u"\u308a"),(u"\u308b\u3046",u"\u308b"),(u"\u308b\u3048",u"\u308c"),(u"\u308b\u304a",u"\u308d"),
       (u"\u3080\u3042",u"\u307e"),(u"\u3080\u3044",u"\u307f"),(u"\u3080\u3046",u"\u3080"),(u"\u3080\u3048",u"\u3081"),(u"\u3080\u304a",u"\u3082"),
       (u"\u306c\u3042",u"\u306a"),(u"\u306c\u3044",u"\u306b"),(u"\u306c\u3046",u"\u306c"),(u"\u306c\u3048",u"\u306d"),(u"\u306c\u304a",u"\u306e"),
       (u"\u3077\u3042",u"\u3071"),(u"\u3077\u3044",u"\u3074"),(u"\u3077\u3046",u"\u3077"),(u"\u3077\u3048",u"\u307a"),(u"\u3077\u304a",u"\u307d"),
       (u"\u3059\u3042",u"\u3055"),(u"\u3059\u3046",u"\u3059"),(u"\u3059\u3048",u"\u305b"),(u"\u3059\u304a",u"\u305d"),
       (u"\u3057\u3085\u3042",u"\u3057\u3083"),(u"\u3057\u3085\u3044",u"\u3057"),(u"\u3057\u3085\u3046",u"\u3057\u3085"),(u"\u3057\u3085\u3048",u"\u3057\u3047"),(u"\u3057\u3085\u304a",u"\u3057\u3087"),
       (u"\u3064\u3042",u"\u305f"),(u"\u3064\u3044",u"\u3061"),(u"\u3064\u3046",u"\u3064"),(u"\u3064\u3048",u"\u3066"),(u"\u3064\u304a",u"\u3068"),
       (u"\u3086\u3042",u"\u3084"),(u"\u3086\u3046",u"\u3086"),(u"\u3086\u3048",u"\u3044\u3047"),(u"\u3086\u304a",u"\u3088"),
       (u"\u305a\u3042",u"\u3056"),(u"\u305a\u3044",u"\u3058"),(u"\u305a\u3046",u"\u305a"),(u"\u305a\u3048",u"\u305c"),(u"\u305a\u304a",u"\u305e"),
       (u"\u308f\u3042",u"\u308f"),(u"\u308f\u3044",u"\u3046\u3043"),(u"\u308f\u3046",u"\u3046"),(u"\u308f\u3048",u"\u3046\u3047"),(u"\u308f\u304a",u"\u3092"),
       (u'\u3046\u3043\u3066\u3085', u'\u3046\u3043\u3065'), # sounds a bit better for words like 'with'
       (u'\u3050\u3050',u'\u3050'), # gugu -> gu, sometimes comes up with 'gl-' combinations
    ],
  ),
  "names" : makeDic(
    "Lexconvert internal phoneme names (sometimes useful with the --phones option while developing new formats)",
     *[(phName,phVal) for phName,phVal in phonemes.items()]),
}

# The mainopt() functions are the main options
# (if you implement a new one, main() will detect it);
# 1st line of doc string should be parameter summary
# (start the doc string with \n if no parameters); if 1st
# character of doc string is * then this function is put
# among the first in the help (otherwise alphabetically).
# If function returns a string, that's taken to be a
# message to be printed with error exit.

def mainopt_try(i):
   """*<format> [<pronunciation>]
Convert input from <format> into eSpeak and try it out.
(Requires the 'espeak' command.)
E.g.: python lexconvert.py --try festival h @0 l ou1
 or: python lexconvert.py --try unicode-ipa '\\u02c8\\u0279\\u026adn\\u0329' (for Unicode put '\\uNNNN' or UTF-8)"""
   espeak = convert(getInputText(i+2,"phonemes in "+sys.argv[i+1]+" format"),sys.argv[i+1],'espeak')
   os.popen("espeak -x","w").write(markup_inline_word("espeak",espeak))

def mainopt_trymac(i):
   """*<format> [<pronunciation>]
Convert phonemes from <format> into Mac and try it using the Mac OS 'say' command"""
   mac = convert(getInputText(i+2,"phonemes in "+sys.argv[i+1]+" format"),sys.argv[i+1],'mac')
   os.popen(macSayCommand()+" -v Vicki","w").write(markup_inline_word("mac",mac)) # Need to specify a voice because the default voice might not be able to take Apple phonemes.  Vicki has been available since 10.3, as has the 'say' command (previous versions need osascript, see Gradint's code)

def mainopt_trymac_uk(i):
   """*<format> [<pronunciation>]
Convert phonemes from <format> and try it with Mac OS British voices (see --mac-uk for details)"""
   macuk = convert(getInputText(i+2,"phonemes in "+sys.argv[i+1]+" format"),sys.argv[i+1],'mac-uk')
   m = MacBritish_System_Lexicon("",os.environ.get("MACUK_VOICE","Daniel"))
   try:
      try: m.speakPhones(macuk.split())
      finally: m.close()
   except KeyboardInterrupt:
      sys.stderr.write("Interrupted\n")

def mainopt_phones(i):
   """*<format> [<words>]
Use eSpeak to convert text to phonemes, and then convert the phonemes to format 'format'.
E.g.: python lexconvert.py --phones unicode-ipa This is a test sentence.
(Some commercial speech synthesizers do not work well when driven entirely from phonemes, because their internal format is different and is optimised for normal text.)"""
   format=sys.argv[i+1]
   txt = getInputText(i+2,"text")
   w,r=os.popen4("espeak -q -x",bufsize=max(8192,4*len(txt))) # need to make sure output buffer is big enough (TODO: or use a temp file, or progressive write/read chunks) (as things stand, if bufsize is not big enough, w.close() on the following line can hang, as espeak waits for us to read its output before it can take all of our input)
   w.write(txt) ; w.close()
   response = r.read()
   if not '\n' in response.rstrip() and 'command' in response: return response.strip() # 'bad cmd' / 'cmd not found'
   write_inlineWord_header(format)
   if format=="bbcmicro": write_bbcmicro_phones(response)
   else: print ", ".join([" ".join([markup_inline_word(format,convert(word,"espeak",format)) for word in line.split()]) for line in filter(lambda x:x,response.split("\n"))])

def mainopt_check_variants(i):
   # undocumented (won't appear in help text)
   groups = {}
   for k,v in lexFormats['espeak'].items():
      if type(k)==str:
         intV = int(v)
         if not intV in consonants:
            if not intV in groups: groups[intV] = []
            groups[intV].append((v,k))
   i = groups.items() ; i.sort()
   for k,v in i:
      if len(v)==1: continue
      v.sort()
      while True:
         print "Group",k
         os.popen("espeak -x","w").write('\n'.join([markup_inline_word("espeak",w) for _,w in v]))
         if not input("Again? 1/0: "): break

def mainopt_convert(i):
   """*<from-format> <to-format>
Convert a user lexicon file.  Expects Festival's .festivalrc to be in the home directory, or espeak's en_extra or Cepstral's lexicon.txt to be in the current directory.
For InfoVox/acapela, export the lexicon to acapela.txt in the current directory.
E.g.: python lexconvert.py --convert festival cepstral"""
   fromFormat = sys.argv[i+1]
   toFormat = sys.argv[i+2]
   if fromFormat==toFormat: return "Cannot convert a lexicon to its own format (that could result in it being truncated)"
   if toFormat=="mac-uk": return "Cannot permanently save a Mac-UK lexicon; please use the --mac-uk option to read text"
   try:
      fname=getSetting(toFormat,"lex_filename")
      getSetting(toFormat,"lex_entry_format") # convert_user_lexicon will need this
   except KeyError: return "Write support for lexicons of format '%s' not yet implemented (need at least lex_filename and lex_entry_format); try using --phones or --phones2phones options instead" % (toFormat,)
   if toFormat=="espeak":
      assert fname=="en_extra", "If you changed eSpeak's lex_filename in the table you also need to change the code below"
      try: open("en_list")
      except: return "You should cd to the espeak source directory before running this"
      os.system("mv en_extra en_extra~ ; grep \" // \" en_extra~ > en_extra") # keep the commented entries, so can incrementally update the user lexicon only
      outFile=open(fname,"a")
   else:
      l = 0
      try: l = open(fname).read()
      except: pass
      assert not l, "File "+fname+" already exists and is not empty; are you sure you want to overwrite it?  (Delete it first if so)" # (if you run with python -O then this is ignored, as are some other checks so be careful)
      outFile=open(fname,"w")
   print "Writing lexicon entries to",fname
   convert_user_lexicon(fromFormat,toFormat,outFile)
   fileLen = outFile.tell()
   outFile.close()
   if toFormat=="bbcmicro": print_bbclex_instructions(fname,fileLen)
   if toFormat=="espeak": os.system("espeak --compile=en")

def mainopt_festival_dictionary_to_espeak(i):
   """<location>
Convert the Festival Oxford Advanced Learners Dictionary (OALD) pronunciation lexicon to ESpeak.
You need to specify the location of the OALD file in <location>,
e.g. for Debian festlex-oald package: python lexconvert.py --festival-dictionary-to-espeak /usr/share/festival/dicts/oald/all.scm
or if you can't install the Debian package, try downloading http://ftp.debian.org/debian/pool/non-free/f/festlex-oald/festlex-oald_1.4.0.orig.tar.gz, unpack it into /tmp, and do: python lexconvert.py --festival-dictionary-to-espeak /tmp/festival/lib/dicts/oald/oald-0.4.out
In all cases you need to cd to the espeak source directory before running this.  en_extra will be overwritten.  Converter will also read your ~/.festivalrc if it exists.  (You can later incrementally update from ~/.festivalrc using the --convert option; the entries from the system dictionary will not be overwritten in this case.)  Specify --without-check to bypass checking the existing espeak pronunciation for OALD entries (much faster, but makes a larger file and in some cases compromises the pronunciation quality)."""
   try: festival_location=sys.argv[i]
   except IndexError: return "Error: --festival-dictionary-to-espeak must be followed by the location of the festival OALD file (see help text)"
   try: open(festival_location)
   except: return "Error: The specified OALD location '"+festival_location+"' could not be opened"
   try: open("en_list")
   except: return "Error: en_list could not be opened (did you remember to cd to the eSpeak dictsource directory first?"
   convert_system_festival_dictionary_to_espeak(festival_location,not '--without-check' in sys.argv,not os.system("test -e ~/.festivalrc"))

def mainopt_syllables(i):
   """[<words>]
Attempt to break 'words' into syllables for music lyrics (uses espeak to determine how many syllables are needed)"""
   txt=getInputText(i+1,"word(s)");words=txt.split()
   w,r=os.popen4("espeak -q -x",bufsize=max(8192,4*len(txt))) # TODO: same as above (bufsize)
   w.write('\n'.join(words).replace("!","").replace(":","")) ; w.close()
   response = r.read()
   if not '\n' in response.rstrip() and 'command' in response: return response.strip() # 'bad cmd' / 'cmd not found'
   rrr = response.split("\n")
   print " ".join([hyphenate(word,sylcount(convert(line,"espeak","festival"))) for word,line in zip(words,filter(lambda x:x,rrr))])

def mainopt_phones2phones(i):
   """*<format1> <format2> [<phonemes in format1>]
Perform a one-off conversion of phonemes from format1 to format2"""
   format1,format2 = sys.argv[i+1],sys.argv[i+2]
   text=getInputText(i+3,"phonemes in "+format1+" format")
   if checkSetting(format1,'space_separates_words_not_phonemes'):
      for w in text.split(): print markup_inline_word(format2, convert(w,format1,format2))
   else: print markup_inline_word(format2, convert(text,format1,format2))

def mainopt_mac_uk(i):
   """<from-format> [<text>]
Speak text in Mac OS 10.7+ British voices while using a lexicon converted in from <from-format>. As these voices do not have user-modifiable lexicons, lexconvert must binary-patch your system's master lexicon; this is at your own risk! (Superuser privileges are needed the first time. A backup of the system file is made, and all changes are restored on normal exit but if you force-quit then you might need to restore the backup manually. Text speaking needs to be under lexconvert's control because it usually has to change the input words to make them fit the available space in the binary lexicon.) By default the Daniel voice is used; Emily or Serena can be selected by setting the MACUK_VOICE environment variable."""
   fromFormat = sys.argv[i+1]
   lex = get_macuk_lexicon(fromFormat)
   m = MacBritish_System_Lexicon(getInputText(i+2,"text"),os.environ.get("MACUK_VOICE","Daniel"))
   try:
      try: m.readWithLex(lex)
      finally: m.close()
   except KeyboardInterrupt:
      sys.stderr.write("Interrupted\n")

class Counter(object):
    "A simple class with two static members, count and subcount, for use by the consonant(), vowel() and other() functions"
    c=sc=0
def other():
    "Used by Phonemes() when creating something that is neither a vowel nor a consonant, e.g. a stress mark"
    Counter.c += 1 ; Counter.sc=0 ; return Counter.c
consonants = set() ; mainVowels = set()
def consonant():
    "Used by Phonemes() when creating a consonant"
    r = other() ; consonants.add(r) ; return r
def vowel():
    "Used by Phonemes() when creating a vowel"
    r = other() ; mainVowels.add(r) ; return r
def opt_vowel():
    "Used by Phonemes() when creating an optional vowel (one that has no warning issued if some format doesn't support it)"
    return other()
def variant():
    "Used by Phonemes() when creating a variant of the just-defined vowel/consonant/etc"
    Counter.sc += 1
    while str(Counter.sc).endswith('0'): Counter.sc += 1
    return 0, float('%d.%d' % (Counter.c,Counter.sc))
    # the 0 is so we can say _, name = variant()
    # so as to get some extra indentation

def ifset(var,a,b=""):
   "Checks the environment variable var; if it is set (non-empty), return a, otherwise return b.  Used in LexFormats to create tables with variations set by the environment."
   import os
   if os.environ.get(var,""): return a
   else: return b

def makeDic(doc,*args,**kwargs):
    "Make a dictionary with a doc string, default-bidirectional mappings and extra settings; see LexFormats for how this is used."
    d = {("settings","doc"):doc} ; duplicates = []
    for a in args:
        assert type(a)==tuple and (len(a)==2 or len(a)==3)
        k=a[0]
        if k in d: duplicates.append(k)
        v=a[1] ; d[k] = v
        if len(a)==3: bidir=a[2]
        else: bidir=True
        if bidir:
            # (k,v,True) = both (k,v) and (v,k)
            if v in d: duplicates.append(v)
            d[v] = k
    missing = [l for l in (list(consonants)+list(mainVowels)) if not l in d]
    if missing:
       import sys ; sys.stderr.write("WARNING: Some non-optional vowels/consonants are missing from "+repr(doc)+"\nThe following are missing: "+", ".join("/".join(g for g,val in globals().items() if val==m) for m in missing)+"\n")
    assert not duplicates, " Duplicate key(s) in "+repr(doc)+": "+", ".join((repr(dup)+"".join(" (="+g+")" for g,val in globals().items() if val==dup)) for dup in sorted(duplicates))+". Did you forget a ,False to suppress bidirectional mapping?" # by the way, Python does not detect duplicate keys in {...} notation - it just lets you overwrite
    for k,v in kwargs.items(): d[('settings',k)] = v
    global lastDictionaryMade ; lastDictionaryMade = d
    return d
def makeVariantDic(doc,*args,**kwargs):
    "Like makeDic but create a new 'variant' version of the last-made dictionary, modifying some phonemes and settings (and giving it a new doc string) but keeping everything else the same.  Any list settings (e.g. cleanup_regexps) are ADDED to by the variant; other settings and phonemes are REPLACED if they are specified in the variant."
    toUpdate = lastDictionaryMade.copy()
    global mainVowels,consonants
    oldV,oldC = mainVowels,consonants
    mainVowels,consonants = [],[] # so makeDic doesn't complain if some vowels/consonants are missing
    d = makeDic(doc,*args,**kwargs)
    mainVowels,consonants = oldV,oldC
    for k,v in toUpdate.items():
       if type(v)==list and k in d: d[k] = v+d[k]
    toUpdate.update(d) ; return toUpdate
def getSetting(formatName,settingName):
  "Gets a setting from lexFormats, exception if not there"
  return lexFormats[formatName][('settings',settingName)]
def checkSetting(formatName,settingName,default=""):
  "Gets a setting from lexFormats, default if not there"
  return lexFormats[formatName].get(('settings',settingName),default)
lexFormats = LexFormats()

import commands,sys,re,os

cached_sourceName,cached_destName,cached_dict = None,None,None
def make_dictionary(sourceName,destName):
    "Uses lexFormats to make a mapping dictionary from a particular source format to a particular dest format, and also sets module variables for that particular conversion (TODO: put those module vars into an object in case someone wants to use this code in a multithreaded server)"
    global cached_sourceName,cached_destName,cached_dict
    if (sourceName,destName) == (cached_sourceName,cached_destName): return cached_dict
    source = lexFormats[sourceName]
    dest = lexFormats[destName]
    d = {}
    global dest_consonants ; dest_consonants = set()
    global dest_syllable_sep ; dest_syllable_sep = dest.get(syllable_separator,"")
    global implicit_vowel_before_NL
    implicit_vowel_before_NL = None
    for k,v in source.items():
      if type(k)==tuple: continue # settings
      if type(v) in [str,unicode]: continue # (num->string entries are for converting IN to source; we want the string->num entries for converting out)
      if not v in dest: v = int(v) # (try the main version of a variant)
      if not v in dest: continue # (haven't got it - will have to ignore or break into parts)
      d[k] = dest[v]
      if int(v) in consonants: dest_consonants.add(d[k])
      if int(v)==e_as_in_herd and (not implicit_vowel_before_NL or v==int(v)): # TODO: or u_as_in_but ?  used by festival and some other synths before words ending 'n' or 'l' (see usage of implicit_vowel_before_NL later)
        implicit_vowel_before_NL = d[k]
    cached_sourceName,cached_destName,cached_dict=sourceName,destName,d
    return d

warnedAlready = set()
def convert(pronunc,source,dest):
    "Convert pronunc from source to dest"
    if source==dest: return pronunc # essential for --try experimentation with codes not yet supported by lexconvert
    if source=="unicode-ipa":
        # try to decode it
        if "\\u" in pronunc and not '"' in pronunc: # maybe \uNNNN copied from Gecko on X11, can just evaluate it to get the unicode
            # (NB make sure to quote the \'s if pasing in on the command line)
            try: pronunc=eval('u"'+pronunc+'"')
            except: pass
        else: # see if it makes sense as utf-8
            try: pronunc = pronunc.decode('utf-8')
            except: pass
    ret = [] ; toAddAfter = None
    dictionary = make_dictionary(source,dest)
    maxLen=max(len(l) for l in dictionary.keys())
    debugInfo=""
    safe_to_drop = checkSetting(source,"safe_to_drop_characters")
    for s,r in checkSetting(source,'cvtOut_regexps'):
        pronunc=re.sub(s,r,pronunc)
    while pronunc:
        for lettersToTry in range(maxLen,-1,-1):
            if not lettersToTry:
              if safe_to_drop==True: pass
              elif (not safe_to_drop) or not pronunc[0] in safe_to_drop and not (pronunc[0],debugInfo) in warnedAlready:
                 warnedAlready.add((pronunc[0],debugInfo))
                 sys.stderr.write("Warning: ignoring "+source+" character "+repr(pronunc[0])+debugInfo+" (unsupported in "+dest+")\n")
              pronunc=pronunc[1:] # ignore
            elif dictionary.has_key(pronunc[:lettersToTry]):
                debugInfo=" after "+pronunc[:lettersToTry]
                toAdd=dictionary[pronunc[:lettersToTry]]
                isStressMark=(toAdd and toAdd in [lexFormats[dest].get(primary_stress,''),lexFormats[dest].get(secondary_stress,''),lexFormats[dest].get(syllable_separator,'')])
                if isStressMark and not checkSetting(dest,"stress_comes_before_vowel"):
                    if checkSetting(source,"stress_comes_before_vowel"): toAdd, toAddAfter = "",toAdd # move stress marks from before vowel to after
                    else:
                        # With Cepstral synth, stress mark should be placed EXACTLY after the vowel and not any later.  Might as well do this for others also.
                        r=len(ret)-1
                        while ret[r] in dest_consonants or ret[r].endswith("*added"): r -= 1 # (if that raises IndexError then the input had a stress mark before any vowel) ("*added" condition is there so that implicit vowels don't get the stress)
                        ret.insert(r+1,toAdd) ; toAdd=""
                elif isStressMark and not checkSetting(source,"stress_comes_before_vowel"): # it's a stress mark that should be moved from after the vowel to before it
                    i=len(ret)
                    while i and (ret[i-1] in dest_consonants or ret[i-1].endswith("*added")): i -= 1
                    if i: i-=1
                    ret.insert(i,toAdd)
                    if dest_syllable_sep: ret.append(dest_syllable_sep) # (TODO: this assumes stress marks are at end of syllable rather than immediately after vowel; correct for Festival; check others; probably a harmless assumption though; mac-uk is better with syllable separators although espeak basically ignores them)
                    toAdd = ""
                # attempt to sort out the festival dictionary's (and other's) implicit_vowel_before_NL
                elif implicit_vowel_before_NL and ret and ret[-1] and toAdd in ['n','l'] and ret[-1] in dest_consonants: ret.append(implicit_vowel_before_NL+'*added')
                elif len(ret)>2 and ret[-2].endswith('*added') and toAdd and not toAdd in dest_consonants and not toAdd==dest_syllable_sep: del ret[-2]
                if toAdd:
                    # Add it, but if toAdd is multiple phonemes, try to put toAddAfter after the FIRST phoneme
                    toAdd=toAdd.split() # TODO: this works only when converting to formats where space_separates_words_not_phonemes==False (doesn't really matter for eSpeak though)
                    ret.append(toAdd[0])
                    if toAddAfter and not toAdd[0] in dest_consonants:
                        ret.append(toAddAfter)
                        toAddAfter=None
                    ret += toAdd[1:]
                pronunc=pronunc[lettersToTry:]
                break
    if toAddAfter: ret.append(toAddAfter)
    if ret and ret[-1]==dest_syllable_sep: del ret[-1] # spurious syllable separator at end
    if checkSetting(dest,'space_separates_words_not_phonemes'): separator = ''
    else: separator = ' '
    ret=separator.join(ret).replace('*added','')
    for s,r in checkSetting(dest,'cleanup_regexps'):
      ret=re.sub(s,r,ret)
    if type(ret)==unicode and os.environ.get("KANA_TYPE","").lower().startswith("k"): ret=hiragana_to_katakana(ret)
    return ret

def hiragana_to_katakana(u):
   "Converts all hiragana characters in unicode string 'u' into katakana"
   assert type(u)==unicode
   if not re.search(u'[\u3041-\u3096]',u): return u
   u = list(u)
   for i in xrange(len(u)):
      if 0x3041 <= ord(u[i]) <= 0x3096:
         u[i]=unichr(ord(u[i])+0x60)
   return u"".join(u)

def espeak_probably_right_already(existing_pronunc,new_pronunc):
    """Used by convert_system_festival_dictionary_to_espeak to compare a "new" pronunciation with eSpeak's existing pronunciation.  As the transcription from OALD to eSpeak is only approximate, it could be that our new pronunciation is not identical to the existing one but the existing one is actually correct; try to detect when this happens by checking if the pronunciations are the same after some simplifications."""
    if existing_pronunc==new_pronunc: return True
    def simplify(pronunc): return \
        pronunc.replace(";","").replace("%","") \
        .replace("a2","@") \
        .replace("3","@") \
        .replace("L","l") \
        .replace("I2","i:") \
        .replace("I","i:").replace("i@","i:@") \
        .replace(",","") \
        .replace("s","z") \
        .replace("aa","A:") \
        .replace("A@","A:") \
        .replace("O@","O:") \
        .replace("o@","O:") \
        .replace("r-","r")
    # TODO: rewrite @ to 3 whenever not followed by a vowel?
    if simplify(existing_pronunc)==simplify(new_pronunc): return True # almost the same, and festival @/a2 etc seems to be a bit ambiguous so leave it alone

def parse_festival_dict(festival_location):
    "For OALD; yields word,part-of-speech,pronunciation"
    ret = []
    for line in open(festival_location).xreadlines():
        line=line.strip()
        if "((pos" in line: line=line[:line.index("((pos")]
        if line.startswith('( "'): line=line[3:]
        line=line.replace('"','').replace('(','').replace(')','')
        try:
            word, pos, pronunc = line.split(None,2)
        except ValueError: continue # malformed line
        if pos not in ['n','v','a','cc','dt','in','j','k','nil','prp','uh']: continue # two or more words
        yield (word.lower(), pos, pronunc)

def convert_system_festival_dictionary_to_espeak(festival_location,check_existing_pronunciation,add_user_dictionary_also):
    "See mainopt_festival_dictionary_to_espeak"
    os.system("mv en_extra en_extra~") # start with blank 'extra' dictionary
    if check_existing_pronunciation: os.system("espeak --compile=en") # so that the pronunciation we're checking against is not influenced by a previous version of en_extra
    outFile=open("en_extra","w")
    print "Reading dictionary lists"
    wordDic = {} ; ambiguous = {}
    for line in filter(lambda x:x.split() and not re.match(r'^[a-z]* *\$',x),open("en_list").read().split('\n')): ambiguous[line.split()[0]]=ambiguous[line.split()[0]+'s']=True # this stops the code below from overriding anything already in espeak's en_list.  If taking out then you need to think carefully about words like "a", "the" etc.
    for word,pos,pronunc in parse_festival_dict(festival_location):
        pronunc=pronunc.replace("i@ 0 @ 0","ii ou 2 ").replace("i@ 0 u 0","ii ou ") # (hack for OALD's "radio"/"video"/"stereo"/"embryo" etc)
        pronunc=pronunc.replace("0","") # 0's not necessary, and OALD sometimes puts them in wrong places, confusing the converter
        if wordDic.has_key(word):
            ambiguous[word] = True
            del wordDic[word] # better not go there
        if not ambiguous.has_key(word):
            wordDic[word] = (pronunc, pos)
    toDel = []
    if check_existing_pronunciation:
        print "Checking existing pronunciation"
        proc=os.popen("espeak -q -x -v en-rp > /tmp/.pronunc 2>&1","w")
        wList = []
    progressCount=0 ; oldPercent=-1
    for word,(pronunc,pos) in wordDic.items():
        if check_existing_pronunciation:
            percent = int(progressCount*100/len(wordDic))
            if not percent==oldPercent: sys.stdout.write(str(percent)+"%\r") ; sys.stdout.flush()
            oldPercent=percent
            progressCount += 1
        if not re.match("^[A-Za-z]*$",word): # (some versions of eSpeak also OK with "-", but not all)
            # contains special characters - better not go there
            toDel.append(word)
        elif word.startswith("plaque") or word in "friday saturday sunday tuesday thursday yesterday".split():
            # hack to accept eSpeak's pl'ak instead of pl'A:k - order was reversed in the March 2009 draft
            toDel.append(word)
        elif word[-1]=="s" and wordDic.has_key(word[:-1]):
            # unnecessary plural (espeak will pick up on them anyway)
            toDel.append(word)
        elif word.startswith("year") or "quarter" in word: toDel.append(word) # don't like festival's pronunciation of those (TODO: also 'memorial' why start with [m'I])
        elif check_existing_pronunciation:
            proc.write(word+"\n")
            proc.flush() # so the progress indicator works
            wList.append(word)
    if check_existing_pronunciation:
        proc.close() ; print
        oldPronDic = {}
        for k,v in zip(wList,open("/tmp/.pronunc").read().split("\n")): oldPronDic[k]=v.strip().replace(" ","")
    for w in toDel: del wordDic[w]
    print "Doing the conversion"
    lines_output = 0
    total_lines = 0
    not_output_because_ok = []
    items = wordDic.items() ; items.sort() # necessary because of the hacks below which check for the presence of truncated versions of the word (want to have decided whether or not to output those truncated versions before reaching the hacks)
    for word,(pronunc,pos) in items:
        total_lines += 1
        new_e_pronunc = convert(pronunc,"festival","espeak")
        if new_e_pronunc.count("'")==2 and not '-' in word: new_e_pronunc=new_e_pronunc.replace("'",",",1) # if 2 primary accents then make the first one a secondary (except on hyphenated words)
        # TODO if not en-rp? - if (word.endswith("y") or word.endswith("ie")) and new_e_pronunc.endswith("i:"): new_e_pronunc=new_e_pronunc[:-2]+"I"
        unrelated_word = None
        if check_existing_pronunciation: espeakPronunc = oldPronDic.get(word,"")
        else: espeakPronunc = ""
        if word[-1]=='e' and wordDic.has_key(word[:-1]): unrelated_word, espeakPronunc = word[:-1],"" # hack: if word ends with 'e' and dropping the 'e' leaves a valid word that's also in the dictionary, we DON'T want to drop this word on the grounds that espeak already gets it right, because if we do then adding 's' to this word may cause espeak to add 's' to the OTHER word ('-es' rule).
        if espeak_probably_right_already(espeakPronunc,new_e_pronunc):
            not_output_because_ok.append(word)
            continue
        if not unrelated_word: lines_output += 1
        outFile.write(word+" "+new_e_pronunc+" // from Festival's ("+pronunc+")")
        if espeakPronunc: outFile.write(", not [["+espeakPronunc+"]]")
        elif unrelated_word: outFile.write(" (here to stop espeak's affix rules getting confused by Festival's \""+unrelated_word+"\")")
        outFile.write("\n")
    print "Corrected(?) %d entries out of %d" % (lines_output,total_lines)
    if add_user_dictionary_also: convert_user_lexicon("festival","espeak",outFile)
    outFile.close()
    os.system("espeak --compile=en")
    if not_output_because_ok:
      print "Checking for unwanted side-effects of those corrections" # e.g. terrible as Terr + ible, inducing as in+Duce+ing
      proc=os.popen("espeak -q -x -v en-rp > /tmp/.pronunc 2>&1","w")
      progressCount = 0
      for w in not_output_because_ok:
          proc.write(w+"\n") ; proc.flush()
          percent = int(progressCount*100/len(not_output_because_ok))
          if not percent==oldPercent: sys.stdout.write(str(percent)+"%\r") ; sys.stdout.flush()
          oldPercent = percent
          progressCount += 1
      proc.close()
      outFile=open("en_extra","a") # append to it
      for word,pronunc in zip(not_output_because_ok,open("/tmp/.pronunc").read().split("\n")):
        pronunc = pronunc.strip().replace(" ","")
        if not pronunc==oldPronDic[word] and not espeak_probably_right_already(oldPronDic[word],pronunc):
          outFile.write(word+" "+oldPronDic[word]+" // (undo affix-side-effect from previous words that gave \""+pronunc+"\")\n")
      outFile.close()
      os.system("espeak --compile=en")
    return not_output_because_ok

def read_user_lexicon(fromFormat):
    "Calls the appropriate lex_read_function, opening lex_filename first if supplied"
    readFunction = checkSetting(fromFormat,"lex_read_function")
    if not readFunction: raise Exception("Reading from '%s' lexicon file not yet implemented (no lex_read_function); try using --phones or --phones2phones options instead" % (fromFormat,))
    try:
       lexFilename = getSetting(fromFormat,"lex_filename")
       lexfile = open(lexFilename)
    except KeyError: lexfile = None # lex_read_function without lex_filename is allowed, if the read function can take null param and fetch the lexicon itself
    return readFunction(lexfile)

def get_macuk_lexicon(fromFormat):
    "Converts lexicon from fromFormat and returns a list suitable for MacBritish_System_Lexicon's readWithLex"
    return [(word,convert(pronunc,fromFormat,"mac-uk")) for word, pronunc in read_user_lexicon(fromFormat)]

def convert_user_lexicon(fromFormat,toFormat,outFile):
    "See mainopt_convert"
    lex = read_user_lexicon(fromFormat)
    if toFormat=="bbcmicro": bbc_prepDefaultLex(outFile)
    outFile.write(checkSetting(toFormat,"lex_header"))
    entryFormat=getSetting(toFormat,"lex_entry_format")
    wordCase=checkSetting(toFormat,"lex_word_case")
    for word, pronunc in lex:
        pronunc = convert(pronunc,fromFormat,toFormat)
        if type(pronunc)==unicode: pronunc=pronunc.encode('utf-8')
        if wordCase=="upper": word=word.upper()
        elif wordCase=="lower": word=word.lower()
        outFile.write(entryFormat % (word,pronunc))
    if toFormat=="bbcmicro": bbc_appendDefaultLex(outFile)
    outFile.write(checkSetting(toFormat,"lex_footer"))

def write_inlineWord_header(format):
    "Checks the format for inline_header, prints if so"
    h = checkSetting(format,"inline_header")
    if h: print h
bbc_charsSoFar=0 # hack for bbcmicro
def markup_inline_word(format,pronunc):
    "Returns pronunc with any necessary markup for putting it in a text (using the inline_format setting).  Contains special-case code for bbcmicro (beginning a new *SPEAK command when necessary)"
    if type(pronunc)==unicode: pronunc=pronunc.encode('utf-8') # UTF-8 output - ok for pasting into Firefox etc *IF* the terminal/X11 understands utf-8 (otherwise redirect to a file, point the browser at it, and set encoding to utf-8, or try --convert'ing which will o/p HTML)
    if format=="bbcmicro":
      global bbc_charsSoFar
      if not bbc_charsSoFar or bbc_charsSoFar+len(pronunc) > 165: # 238 is max len of the immediate BASIC prompt, but get a "Line too long" message from Speech if go over 165 including the '*SPEAK ' (158 excluding it).
        if bbc_charsSoFar: r="\n"
        else: r=""
        bbc_charsSoFar = 7+len(pronunc)+1 # +1 for the space after this word.
        return r+"*SPEAK "+pronunc
      else:
        bbc_charsSoFar += len(pronunc)+1
        return pronunc
    return checkSetting(format,"inline_format","%s") % pronunc

def sylcount(festival):
  """Tries to count the number of syllables in a Festival string (see mainopt_syllables).  We treat @ as counting the same as the previous syllable (e.g. "fire", "power"), but this can vary in different songs, so the result will likely need a bit of proofreading."""
  count = inVowel = maybeCount = hadAt = 0
  festival = festival.split()
  for phone,i in zip(festival,range(len(festival))):
    if phone[0] in "aeiou": inVowel=0 # unconditionally start new syllable
    if phone[0] in "aeiou@12":
      if not inVowel: count += 1
      elif phone[0]=="@" and not hadAt: maybeCount = 1 # (e.g. "loyal", but NOT '1', e.g. "world")
      if "@" in phone: hadAt = 1 # for words like "cheerful" ("i@ 1 @" counts as one)
      inVowel = 1
      if phone[0]=="@" and i>=3 and festival[i-2:i]==["ai","1"] and festival[i-3] in ["s","h"]: # special rule for higher, Messiah, etc - like "fire" but usually 2 syllables
        maybeCount = 0 ; count += 1
    else:
      if not phone[0] in "drz": count += maybeCount # not 'r/z' e.g. "ours", "fired" usually 1 syllable in songs, "desirable" usually 4 not 5
      # TODO steward?  y u@ 1 d but usally 2 syllables
      inVowel = maybeCount = hadAt = 0
  return count
def hyphenate(word,numSyls):
  "See mainopt_syllables"
  orig = word
  try: word,isu8 = word.decode('utf-8'),True
  except: isu8 = False
  pre=[] ; post=[]
  while word and not 'a'<=word[0].lower()<='z':
    pre.append(word[0]) ; word=word[1:]
  while word and not 'a'<=word[-1].lower()<='z':
    post.insert(0,word[-1]) ; word=word[:-1]
  if numSyls>len(word): return orig # probably numbers or something
  l = int((len(word)+numSyls/2)/numSyls) ; syls = []
  for i in range(numSyls):
    if i==numSyls-1: syls.append(word[i*l:])
    else: syls.append(word[i*l:(i+1)*l])
    if len(syls)>1:
      if len(syls[-1])>2 and syls[-1][0]==syls[-1][1] and not syls[-1][0].lower() in "aeiou":
        # repeated consonant at start - put one on previous
        syls[-2] += syls[-1][0]
        syls[-1] = syls[-1][1:]
      elif ((len(syls[-2])>2 and syls[-2][-1]==syls[-2][-2] and not syls[-2][-1].lower() in "aeiou") \
            or (syls[-1][0].lower() in "aeiouy" and len(syls[-2])>2)) \
            and filter(lambda x:x.lower() in "aeiou",list(syls[-2][:-1])):
        # repeated consonant at end - put one on next
        # or vowel on right: move a letter over (sometimes the right thing to do...)
        # (unless doing so leaves no vowels)
        syls[-1] = syls[-2][-1]+syls[-1]
        syls[-2] = syls[-2][:-1]
  word = ''.join(pre)+"- ".join(syls)+''.join(post)
  if isu8: word=word.encode('utf-8')
  return word

def macSayCommand():
  """Return the environment variable SAY_COMMAND if it is set and if it is non-empty, otherwise return "say".
  E.g. SAY_COMMAND="say -o file.aiff" (TODO: document this in the help text?)
  In Gradint you can set (e.g. if you have a ~/.festivalrc) extra_speech=[("en","python lexconvert.py --mac-uk festival")] ; extra_speech_tofile=[("en",'echo %s | SAY_COMMAND="say -o /tmp/said.aiff" python lexconvert.py --mac-uk festival && sox /tmp/said.aiff /tmp/said.wav',"/tmp/said.wav")]"""
  s = os.environ.get("SAY_COMMAND","")
  if s: return s
  else: return "say"

def getInputText(i,prompt):
  """Gets text either from the command line or from standard input.  Issue prompt if there's nothing on the command line and standard input is connected to a tty instead of a pipe or file."""
  txt = ' '.join(sys.argv[i:])
  if not txt:
    if (not hasattr(sys.stdin,"isatty")) or sys.stdin.isatty(): sys.stderr.write("Enter "+prompt+" (EOF when done)\n")
    txt = sys.stdin.read()
  return txt

def write_bbcmicro_phones(ph):
  """Called by mainopt_phones as a special case because it needs to track the commas to avoid "Line too long"
  (and actually we might as well just put each clause on a separate *SPEAK command, using the natural brief delay between commands; this should minimise the occurrence of additional delays in arbitrary places)
  also calls print_bbc_warnings"""
  totalKeystrokes = 0 ; lines = 0
  for line in filter(lambda x:x,ph.split("\n")):
    global bbc_charsSoFar ; bbc_charsSoFar=0
    l=" ".join([markup_inline_word("bbcmicro",convert(word,"espeak","bbcmicro")) for word in line.split()])
    print l.replace(" \n","\n")
    totalKeystrokes += len(l)+1 ; lines += 1
  print_bbc_warnings(totalKeystrokes,lines)
def print_bbc_warnings(keyCount,lineCount):
  "Print any relevant size warnings regarding sending 'keyCount' keys in 'lineCount' lines to the BBC Micro"
  # and warn if it looks too big:
  limits_exceeded = [] ; severe=0
  if keyCount >= 32768:
    severe=1 ; limits_exceeded.append("BeebEm 32K keystroke limit") # At least in version 3, the clipboard is defined in beebwin.h as a char of size 32768 and its bounds are not checked.  Additionally, if you script a second paste before the first has finished (or if you try to use BeebEm's Copy command) then the first paste will be interrupted.  So if you really want to make BeebEm read more then I suggest setting a printer destination file, putting a VDU 2,10,3 after each batch of commands, and waiting for that \n to appear in that printer file before sending the next batch, or perhaps write a set of programs to a disk image and have them CHAIN each other or whatever.
  shadow_himem=0x8000 # if using a 'shadow mode' on the Master/B+/Integra-B (modes 128-135, which leave all main RAM free)
  mode7_himem=0x7c00 # (40x25 characters = 1000 bytes, by default starting at 7c00 with 24 bytes spare at the top, but the scrolling system uses the full 1024 bytes and can tell the video controller to start rendering at any one of them; if you get Jeremy Ruston's book and program the VIDC yourself then you could fix it at 7c18 if you really want, or just set HIMEM=&8000 and don't touch the screen, but that doesn't give you very much more room)
  default_speech_loc=0x5500
  overhead_per_program_line = 4
  for page,model in [
        (0x1900,"Model B"), # with Acorn DFS (a reasonable assumption although alternate DFS ROMs are different)
        (0xE00,"Master")]: # (the Master has 8k of special paged-in "filing system RAM", so doesn't need 2816 bytes of main RAM for DFS)
     top = page+keyCount+lineCount*(overhead_per_program_line-1)+2 # the -1 is because keyCount includes a carriage return at the end of each line
     if model=="Master": x=" (use Speech's Sideways RAM version instead, e.g. *SRLOAD SP8000 8000 7 and reset, but sound quality might be worse)" # I don't know why but SP8000 can play higher and more distorted than SPEECH, at least on emulation.  Re bank numbers, by default banks 4 to 7 are Sideways RAM (4*16k=64k) and I suppose filling up from 7 makes sense because banks 8-F are ROMs (ANFS,DFS,ViewSheet,Edit,BASIC,ADFS,View,Terminal; OS is a separate 16k so there's scope for 144k of supplied ROM).  Banks 0-3 are ROM expansion slots.  The "128" in the name "Master 128" comes from 32k main RAM, 64k Sideways RAM, 20k shadow RAM (for screen modes 128-135), 4k OS "private RAM" (paged on top of 8000-8FFF) and 8k filing system RAM (paged on top of C000-DFFF) = 128k.  Not sure what happened on the B+.
     else: x=" (Speech program will be overwritten unless relocated)" # (could use Sideways RAM for it instead if you have it fitted, see above)
     if top > default_speech_loc: limits_exceeded.append("%s TOP=&%X limit%s" % (model,default_speech_loc,x)) # The Speech program does nothing to stop your program (or its variables etc) from growing large enough to overwrite &5500, nor does it stop the stack pointer (coming down from HIMEM) from overwriting &72FF. For more safety on a Model B you could use RELOCAT to put Speech at &5E00 and be sure to set HIMEM=&5E00 before loading, but then you must avoid commands that change HIMEM, such as MODE (but selecting any non-shadow mode other than 7 will overwrite Speech anyway, although if you set the mode before loading Speech then it'll overwrite screen memory and still work as long as the affected part of the screen is undisturbed).  You can't do tricks like ditching the lexicon because RELOCAT won't let you go above 5E00 (unless you fix it, but I haven't looked in detail; if you can fix RELOCAT to go above 5E00 then you can create a lexicon-free Speech by taking the 1st 0x1560 bytes of SPEECH and append two * bytes, relocate to &6600 and set HIMEM, but don't expect *SAY to work, unless you put a really small lexicon into the spare 144 bytes that are left - RELOCAT needs an xx00 address so you can't have those bytes at the bottom).  You could even relocate to &6A00 and overwrite (non-shadow) screen memory if you don't mind the screen being filled with gibberish that you'd better not erase! (well if you program the VIDC as mentioned above and you didn't re-add a small lexicon then you could get yourself 3.6 lines of usable Mode 7 display from the spare bytes but it's probably not worth the effort)
     if top > mode7_himem:
        if model=="Master":
           if top > shadow_himem: limits_exceeded.append(model+" 32k HIMEM limit (even for shadow modes)") # I suppose you could try using BAS128 but I doubt it's compatible with Speech.  If you really want to store such a long program on the BBC then you'd better split it into several programs that CHAIN each other (as mentioned above).
           else: limits_exceeded.append(model+" Mode 7 HIMEM limit (use shadow modes 128-135)")
        else: limits_exceeded.append(model+" Mode 7 HIMEM limit") # unless you overwrite the screen (see above) - let's assume the Model B hasn't been fitted with shadow modes (although the Integra-B add-on does give them to the Model B, and leaves PAGE at &1900; B+ has shadow modes but I don't know what's supposed to happen to PAGE on it).  65C02 Tube doesn't help much (it'll try to run Speech on the coprocessor instead of the host, and this results in silence because it can't send its sound back across the Tube; don't know if there's a way to make it run on the host in these circumstances or what the host's memory map is like)
  if lineCount > 32768: limits_exceeded.append("BBC BASIC line number limit") # and you wouldn't get this far without filling the memory, even with 128k (4 bytes per line)
  elif 10*lineCount > 32767: limits_exceeded.append("AUTO line number limit (try AUTO 0,1)") # (default AUTO increments in steps of 10; you can use AUTO 0,1 to start at 0 and increment in steps of 1.  BBC BASIC stores its line info in a compact form which allows a range of 0-32767.)
  if severe: warning,after="WARNING: ",""
  else: warning,after="Note: ","It should still work if pasted into BeebEm as immediate commands. "
  after = ". "+after+"See comments in lexconvert for more details.\n"
  if len(limits_exceeded)>1: sys.stderr.write(warning+"this text may be too big for the BBC Micro. The following limits were exceeded: "+", ".join(limits_exceeded)+after)
  elif limits_exceeded: sys.stderr.write(warning+"this text may be too big for the BBC Micro because it exceeds the "+limits_exceeded[0]+after)
def bbc_prepDefaultLex(outFile):
  """If SPEECH_DISK and MAKE_SPEECH_ROM is set, then read the ROM code from SPEECH_DISK and write to outFile (meant to go before the lexicon, to make a modified BBC Micro Speech ROM with custom lexicon)"""
  if not os.environ.get("MAKE_SPEECH_ROM",0): return
  d=open(os.environ['SPEECH_DISK']).read() # if this fails, SPEECH_DISK was not set or was set incorrectly (it's required for MAKE_SPEECH_ROM)
  i=d.index('LO\x80LP\x80\x82\x11') # start of SP8000 file (if this fails, it wasn't a Speech disk)
  j=d.index('>OUS_',i) # start of lexicon (ditto)
  assert j-i==0x1683, "Is this really an original disk image?"
  outFile.write(d[i:j])
def bbc_appendDefaultLex(outFile,romCode=False):
  """If SPEECH_DISK is set, read Speech's default lexicon from it and append this to outFile (without the terminating >** which is supplied anyway by convert_user_lexicon)"""
  if not os.environ.get("SPEECH_DISK",""): return
  d=open(os.environ['SPEECH_DISK']).read()
  i=d.index('>OUS_') # if this fails, it wasn't a Speech disk
  j=d.index(">**",i)
  assert j-i==2201, "Lexicon on SPEECH_DISK is wrong size (%d). Is this really an original disk image?" % (j-i)
  outFile.write(d[i:j])
  # TODO: can we compress the BBC lexicon?  i.e. detect if a rule will happen anyway due to subsequent wildcard rules, and delete it if so (don't know how many bytes that would save)
  assert not os.environ.get("MAKE_SPEECH_ROM",0) or outFile.tell()+3 <= 16384, "Speech ROM file got too big"

def bbcshortest(n):
  """Convert integer n into the shortest possible number of BBC Micro keystrokes; prefer hex if and only if the extra '&' keystroke won't make it any longer than its decimal equivalent"""
  if len(str(n)) < len('&%X'%n): return str(n)
  else: return '&%X'%n
def bbcKeystrokes(data,start):
  "Return BBC BASIC keystrokes to put data into RAM starting at address start.  Uses BBC assembler instructions, which usually saves keystrokes compared with ! operators.  Keystrokes are limited to ASCII for easier copy/paste."
  i=0 ; ret=[] ; thisLine = ""
  while i<len(data):
    bbc_max_line_len = 238
    def equdParam(): return bbcshortest(ord(data[i])+(ord(data[i+1])<<8)+(ord(data[i+2])<<16)+(ord(data[i+3])<<24))
    def canEQUS(j): return 32<=ord(data[j])<127 and not data[j]=='"' # there aren't any escape sequences to worry about in EQUS strings.  (Delete the <127 if not worried about limiting keystrokes to ASCII.)
    def equsCount(i,lineLeft):
       j=i
       while j<len(data) and j-i<lineLeft-len(':EQUS""') and canEQUS(j): j += 1
       return j-i
    if not thisLine:
       if i==len(data)-4 and not all(canEQUS(j) for j in range(i,len(data))): # finish it off with a pling - it'll be quicker than another "[OPT2:EQUD"
          thisLine='!'+bbcshortest(start)+'='+equdParam()
          break
       elif i==len(data)-1: # ditto with ?
          thisLine='?'+bbcshortest(start)+'='+str(ord(data[i]))
          break
       else: # start the assembler (need a [OPT at the start of each and every line when in immediate mode)
          if not ret: ret.append("P%="+bbcshortest(start))
          thisLine = "[OPT2" # (or OPT1 if you want to see on the screen what it did, but that takes more processing)
    add = equsCount(i,bbc_max_line_len-len(thisLine))
    if add >= 4 or (add >= 2 and len(data)-i < 4): # (a good-enough approximation of when it'll be better to EQUS)
       thisI = ':EQUS"'+data[i:i+add]+'"'
    elif len(data)-i < 4 or equsCount(i+1,bbc_max_line_len) >= 4: # (ditto for EQUB)
       o=ord(data[i]) ; add = 1
       thisI = ':'+{0:"BRK",0x48:"PHA",0x68:"PLA",8:"PHP",0x28:"PLP",0x38:"SEC",0x18:"CLC",0xf8:"SED",0xd8:"CLD",0xe8:"INX",0xca:"DEX",0xc8:"INY",0x88:"DEY",0xaa:"TAX",0xa8:"TAY",0x8a:"TXA",0x98:"TYA",0x9a:"TXS",0xba:"TSX",0xb8:"CLV",0xea:"NOP",0x40:"RTI"}.get(o,"EQUB"+str(o)) # (omit Master-only instructions like 0xda:"PHX") (in extremely rare cases, generating 2, 3 or 4 bytes might just be quicker with opcode+operand than EQUD, e.g. "ROL1:ROL1" vs "EQUD&1260126", but we won't worry about that; anyway most of this stuff will never occur in lexicons and is here only in case bbcKeystrokes ends up being used for something else e.g. the Speech code itself)
    else:
       thisI = ":EQUD"+equdParam() ; add = 4
    if len(thisLine)+len(thisI) <= bbc_max_line_len:
       thisLine += thisI ; i += add ; start += add
    else: # instruction won't fit on current line
       ret.append(thisLine) ; thisLine = "" # and recalculate the instruction on the next loop iter (might then be able to fit more into an EQUS or something)
  if thisLine: ret.append(thisLine)
  return '\n'.join(ret)+'\n'
def print_bbclex_instructions(fname,size):
 """Print suitable instructions for a BBC Micro lexicon of the given filename and size (the exact nature of the instructions depends on the size).  If appropriate, create a .key file containing keystrokes for transferring to an emulator."""
 if os.environ.get("MAKE_SPEECH_ROM",0): print "%s (%d bytes, hex %X) can now installed on an emulator (set in Roms.cfg or whatever), or loaded onto a chip.  The sound quality of this might be worse than that of the main-RAM version." % (fname,size,size) # (at least on emulation - see comment on sound quality above)
 else:
  print "The size of this lexicon is %d bytes (hex %X)" % (size,size)
  bbcStart=None
  noSRAM_lex_offset=0x155F # (on the BBC Micro, SRAM means Sideways RAM, not Static RAM as it does elsewhere; for clarity we'd better say "Sideways RAM" in all output)
  SRAM_lex_offset=0x1683
  SRAM_max=0x4000 # 16k
  noSRAM_default_addr=0x5500
  noSRAM_min_addr=0xE00 # minimum supported by RELOCAT
  page=0x1900 # or 0xE00 for Master (but OK to just leave this at 0x1900 regardless of model; it harmlessly increases the range where special_relocate_instructions 'kick in')
  noSRAM_himem=0x7c00 # unless you're in a shadow mode or something (see comments on himem above), however leaving this at 0x7c00 is usually harmless (just causes the 'need to relocate' to 'kick in' earlier, although if memory is really full it might say 'too big' 1k too early)
  def special_relocate_instructions(reloc_addr):
    pagemove_min,pagemove_max = max(0xE00,page-0x1E00), page+0xE00 # if relocating to within this range, must move PAGE before loading RELOCAT. RELOCAT's supported range is 0xE00 to 0x5E00, omitting (PAGE-&1E00) to (PAGE+&E00)
    if reloc_addr < 0x1900: extra=" On a Model B with Acorn DFS you won't be able to use the disk after relocating below &1900, and you can't run star commands from tape so you have to initialise via CALL. (On a Master, DFS is not affected as it doesn't use &E00-&1900.)"
    else: extra = ""
    if not pagemove_min<=reloc_addr<pagemove_max:
      return extra # no other special instructions needed
    newpage = reloc_addr+0x1E00
    page_max = min(0x5E00,noSRAM_default_addr-0xE00)
    if newpage > page_max: return False # "Unfortunately RELOCAT can't put it at &%X even with PAGE changes." % reloc_addr
    return " Please run RELOCAT with PAGE in the range of &%X to &%X for this relocation to work.%s" % (newpage,page_max,extra)
  if noSRAM_default_addr+noSRAM_lex_offset+size > noSRAM_himem:
    reloc_addr = noSRAM_himem-noSRAM_lex_offset-size
    reloc_addr -= (reloc_addr%256)
    if reloc_addr >= noSRAM_min_addr:
      instr = special_relocate_instructions(reloc_addr)
      if instr==False: print "This lexicon is too big for Speech in main RAM even with relocation, unless RELOCAT is rewritten to work from files."
      else:
        bbcStart = reloc_addr+noSRAM_lex_offset
        reloc_call = reloc_addr + 0xB00
        print "This lexicon is too big for Speech at its default address of &%X, but you could use RELOCAT to put a version at &%X and then initialise it with CALL %s (or do the suggested *SAVE, reset, and run *SP). Be sure to set HIMEM=&%X. Then *LOAD %s %X or change the relocated SP file from offset &%X.%s" % (noSRAM_default_addr,reloc_addr,bbcshortest(reloc_call),reloc_addr,fname,bbcStart,noSRAM_lex_offset,instr)
    else: print "This lexicon is too big for Speech in main RAM even with relocation."
  else:
    bbcStart = noSRAM_default_addr+noSRAM_lex_offset
    print "You can load this lexicon by *LOAD %s %X or change the SPEECH file from offset &%X. Suggest you also set HIMEM=&%X for safety." % (fname,bbcStart,noSRAM_lex_offset,noSRAM_default_addr)
  if bbcStart: # we managed to fit it into main RAM
     keys = bbcKeystrokes(open(fname).read(),bbcStart)
     open(fname+".key","w").write(keys)
     print "For ease of transfer to emulators etc, a self-contained keystroke file for putting %s data at &%X has been written to %s.key" % (fname,bbcStart,fname)
     if len(keys) > 32767: print "(This file looks too big for BeebEm to paste though)" # see comments elsewhere
  # Instructions for replacing lex in SRAM:
  if size > SRAM_max-SRAM_lex_offset: print "This lexicon is too big for Speech in Sideways RAM." # unless you can patch Speech to run in SRAM but read its lexicon from main RAM
  else: print "You can load this lexicon into Sideways RAM by *SRLOAD %s %X 7 (or whichever bank number you're using), or change the SP8000 file from offset &%X." % (fname,SRAM_lex_offset+0x8000,SRAM_lex_offset)
  if not os.environ.get("SPEECH_DISK",""): print "If you want to append the default lexicon to this one, set SPEECH_DISK to the image of the original Speech disk before running lexconvert, e.g. export SPEECH_DISK=/usr/local/BeebEm3/diskimg/Speech.ssd"
  print "You can also set MAKE_SPEECH_ROM=1 (along with SPEECH_DISK) to create a SPEECH.ROM file instead"
 print "If you get 'Mistake in speech' when testing some words, try starting with '*SAY, ' to ensure there's a space at the start of the SAY string (bug in Speech?)" # Can't track down which words this does and doesn't apply to.
 print "It might be better to load your lexicon into eSpeak and use lexconvert's --phones option to drive the BBC with phonemes."

def main():
    """Introspect the module to find the mainopt_ functions, and either call one of them or print the help.  Returns the error code to send back to the OS."""
    def funcToOpt(n): return "--"+n[n.index("_")+1:].replace("_","-")
    for k,v in globals().items():
        if k.startswith('mainopt_') and funcToOpt(k) in sys.argv:
           msg = v(sys.argv.index(funcToOpt(k)))
           if msg:
              sys.stderr.write(msg+"\n") ; return 1
           else: return 0
    html = ('--htmlhelp' in sys.argv) # (undocumented option used for my website, don't rely on it staying)
    def htmlify(h): return h.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('\n','<br>').replace('--','<tt>--</tt>') # (the last bit is so typography.js doesn't try to rewrite options stuff to en-dash)
    if not html: htmlify = lambda x:x
    print htmlify(__doc__)
    if html: missALine = "<p>"
    else: missALine = ""
    print missALine
    if '--formats' in sys.argv: # non-HTML mode only (format descriptions are included in HTML anyway)
       print "Available pronunciation formats:"
       keys=lexFormats.keys() ; keys.sort()
       for k in keys:print "\n"+k+"\n"+getSetting(k,"doc")
       return 0
    elif html:
       print "Available pronunciation formats:"
       if html: print "<table>"
       keys=lexFormats.keys() ; keys.sort()
       for k in keys: print '<tr><td valign="top"><nobr>'+k+'</nobr></td><td valign="top">'+htmlify(getSetting(k,"doc"))+"</td></tr>"
       print "</table>"
    else: print "Available pronunciation formats: "+", ".join(sorted(lexFormats.keys()))+"\n(Use --formats to see their descriptions)"
    print missALine
    print "Program options:"
    print missALine
    if html: print "<dl>"
    for _,opt,desc in sorted([(v.__doc__ and not v.__doc__.startswith('*'),k,v.__doc__) for k,v in globals().items()]):
       if not opt.startswith("mainopt_"): continue
       opt = funcToOpt(opt)
       if not desc: continue # undocumented option
       params,rest = desc.split("\n",1)
       if params.startswith('*'): params=params[1:]
       if params: opt += (' '+params)
       if html: print "<dt>"+htmlify(opt)+"</dt><dd>"+htmlify(rest)+"</dd>"
       else: print opt+"\n"+rest+"\n"
    if html: print "</dl>"
    return 0

catchingSigs = inSigHandler = False
def catchSignals():
  "We had better try to catch all signals if using MacBritish_System_Lexicon so we can safely clean it up. We raise KeyboardInterrupt instead (need to catch this). Might not work with multithreaded code."
  global catchingSigs
  if catchingSigs: return
  catchingSigs = True
  import signal
  def f(sigNo,*args):
    global inSigHandler
    if inSigHandler: return
    inSigHandler = True
    os.killpg(os.getpgrp(),sigNo)
    raise KeyboardInterrupt
  for n in xrange(1,signal.NSIG):
    if not n==signal.SIGCHLD and not signal.getsignal(n)==signal.SIG_IGN:
      try: signal.signal(n,f)
      except: pass
class MacBritish_System_Lexicon(object):
    """Overwrites some of the pronunciations in the system
    lexicon (after backing up the original).  Cannot
    change the actual words in the system lexicon, so just
    alters pronunciations of words you don't intend to use
    so you can substitute these into your texts.
    Restores the lexicon on close()."""
    instances = {}
    def __init__(self,text="",voice="Daniel"):
        """text is the text you want to speak (so that any
        words used in it that are not mentioned in your
        lexicon are unchanged in the system lexicon);
        text="" means you just want to speak phonemes.
        voice can be Daniel, Emily or Serena."""
        self.voice = False
        assert not voice in MacBritish_System_Lexicon.instances, "There is already another instance of MacBritish_System_Lexicon for the "+voice+" voice"
        assert not os.system("lockfile /tmp/"+voice+".PCMWave.lock") # in case some other process has it
        self.voice = voice
        self.filename = "/System/Library/Speech/Voices/"+voice+".SpeechVoice/Contents/Resources/PCMWave"
        assert os.path.exists(self.filename),"Cannot find an installation of '"+voice+"' on this system"
        if not os.path.exists(self.filename+"0"):
            sys.stderr.write("Backing up "+self.filename+" to "+self.filename+"0...\n") # (you'll need a password if you're not running as root)
            err = os.system("sudo mv \""+self.filename+"\" \""+self.filename+"0\"; sudo cp \""+self.filename+"0\" \""+self.filename+"\"; sudo chown "+str(os.getuid())+" \""+self.filename+"\"")
            assert not err, "Error creating backup"
        lexFile = self.filename+".lexdir"
        if not os.path.exists(lexFile):
            sys.stderr.write("Creating lexdir file...\n")
            err = os.system("sudo touch \""+lexFile+"\" ; sudo chown "+str(os.getuid())+" \""+lexFile+"\"")
            assert not err, "Error creating lexdir"
        import cPickle
        if os.stat(lexFile).st_size: self.wordIndexStart,self.wordIndexEnd,self.phIndexStart,self.phIndexEnd = cPickle.Unpickler(open(lexFile)).load()
        else:
            dat = open(self.filename).read()
            def findW(word,rtnPastEnd=0):
                i = re.finditer(re.escape(word+chr(0)),dat)
                try: n = i.next()
                except StopIteration: raise Exception("word not found in voice file")
                try:
                    n2 = i.next()
                    raise Exception("word does not uniquely identify a byte position (has at least %d and %d)" % (n.start(),n2.start()))
                except StopIteration: pass
                if rtnPastEnd: return n.end()
                else: return n.start()
            self.wordIndexStart = findW("808s")
            self.phIndexStart = findW("'e&It.o&U.e&Its")
            self.wordIndexEnd = findW("zombie",1)
            self.phIndexEnd = findW("'zA+m.bI",1)
            cPickle.Pickler(open(lexFile,"w")).dump((self.wordIndexStart,self.wordIndexEnd,self.phIndexStart,self.phIndexEnd)) 
        self.dFile = open(self.filename,'r+')
        assert len(self.allWords()) == len(self.allPh())
        MacBritish_System_Lexicon.instances[voice] = self
        self.textToAvoid = text ; self.restoreDic = {}
        catchSignals()
    def allWords(self):
        "Returns a list of words that are defined in the system lexicon (which won't be changed, but see allPh)"
        self.dFile.seek(self.wordIndexStart)
        return [x for x in self.dFile.read(self.wordIndexEnd-self.wordIndexStart).split(chr(0)) if x]
    def allPh(self):
        "Returns a list of (file position, phoneme string) for each of the primary phoneme entries from the system lexicon.  These entries can be changed in-place by writing to the said file position, and then spoken by giving the voice the corresponding word from allWords (but see also usable_words)."
        self.dFile.seek(self.phIndexStart)
        def f(l):
            last = None ; r = [] ; pos = self.phIndexStart
            for i in l:
                if re.search(r'[ -~]',i) and not i in ["'a&I.'fo&Un","'lI.@n","'so&Un.j$"] and not (i==last and i in ["'tR+e&I.si"]): r.append((pos,i)) # (the listed pronunciations are secondary ones that for some reason are in the list)
                if re.search(r'[ -~]',i): last = i
                pos += (len(i)+1) # +1 for the \x00
            assert pos==self.phIndexEnd+1 # +1 because the last \00 will result in a "" item after; the above +1 will be incorrect for that item
            return r
        return f([x for x in self.dFile.read(self.phIndexEnd-self.phIndexStart).split(chr(0))])
    def usable_words(self,words_ok_to_redefine=[]):
        "Returns a list of (word,phoneme_file_position,original_phonemes) by combining allWords with allPh, but omitting any words that don't seem 'usable' (for example words that contain spaces, since these lexicon entries don't seem to be actually used by the voice).  Words that occur in self.textToAvoid are also considered non-usable, unless they also occur in words_ok_to_redefine (user lexicon)."
        for word,(pos,phonemes) in zip(self.allWords(),self.allPh()):
            if not re.match("^[a-z0-9]*$",word): continue # it seems words not matching this regexp are NOT used by the engine
            if not (phonemes and 32<ord(phonemes[0])<127): continue # better not touch those, just in case
            if word in self.textToAvoid and not word in words_ok_to_redefine: continue
            yield word,pos,phonemes
    def check_redef(self,wordsAndPhonemes):
        "Diagnostic function to list on standard error the redefinitions we want to make.  wordsAndPhonemes is a list of (original system-lexicon word, proposed new phonemes).  The old phonemes are also listed, fetched from allPh."
        aw = self.allWords() ; ap = 0
        for w,p in wordsAndPhonemes:
          w = w.lower()
          if not re.match("^[a-z0-9]*$",w): continue
          if not w in aw: continue
          if not ap:
            ap = self.allPh()
            sys.stderr.write("Warning: some words were already in system lexicon\nword\told\tnew\n")
          sys.stderr.write(w+"\t"+ap[aw.index(w)][1]+"\t"+p+"\n")
    def speakPhones(self,phonesList):
        "Speaks every phonetic word in phonesList"
        words = [str(x)+"s" for x in range(len(phonesList))]
        d = self.setMultiple(words,phonesList)
        os.popen(macSayCommand()+" -v \""+self.voice+"\"",'w').write(" ".join(d.get(w,"") for w in words))
    def readWithLex(self,lex):
        "Reads the text given in the constructor after setting up the lexicon with the given (word,phoneme) list"
        # self.check_redef(lex) # uncomment if you want to know about these
        tta = ' '+self.textToAvoid.replace(u'\u2019'.encode('utf-8'),"'")+' '
        words2,phonemes2 = [],[] # keep only the ones actually used in the text (no point setting whole lexicon)
        nonWordBefore=r"(?i)(?<=[^A-Za-z"+chr(0)+"])" # see below for why chr(0) is included; (?i) = ignore case
        nonWordAfter=r"(?=([^A-Za-z']|'[^A-Za-z]))" # followed by non-letter non-apostrophe, or followed by apostrophe non-letter (so not if followed by "'s")
        for ww,pp in lex:
          if re.search(nonWordBefore+re.escape(ww)+nonWordAfter,tta):
            words2.append(ww) ; phonemes2.append(pp)
        for k,v in self.setMultiple(words2,phonemes2).iteritems(): tta = re.sub(nonWordBefore+re.escape(k)+nonWordAfter,chr(0)+v,tta)
        tta = tta.replace(chr(0),'')
        os.popen(macSayCommand()+" -v \""+self.voice+"\"",'w').write(tta)
    def setMultiple(self,words,phonemes):
        "Sets phonemes for words, returning dict of word to substitute word.  Flushes file buffer before return."
        avail = [] ; needed = []
        for word,pos,phon in self.usable_words(words):
            avail.append((len(phon),word,pos,phon))
        for word,phon in zip(words,phonemes):
            needed.append((len(phon),word,phon))
        avail.sort() ; needed.sort() # shortest phon first
        i = 0 ; wDic = {}
        for l,word,phon in needed:
            while avail[i][0] < l:
                i += 1
                if i==len(avail):
                    sys.stderr.write("Could not find enough lexicon slots!\n") # TODO: we passed 'words' to usable_words's words_ok_to_redefine - this might not be the case if we didn't find enough slots
                    self.dFile.flush() ; return wDic
            _,wSubst,pos,oldPhon = avail[i] ; i += 1
            if avail[i][2] in self.restoreDic: oldPhon=None # shouldn't happen if setMultiple is called only once, but might be useful for small experiments in the Python interpreter etc
            self.set(pos,phon,oldPhon)
            wDic[word] = wSubst
        self.dFile.flush() ; return wDic
    def set(self,phPos,val,old=None):
        """Sets phonemes at position phPos to new value.
        Caller should flush the file buffer when done."""
        # print "Debugger: setting %x to %s" % (phPos,val)
        if old:
            assert not phPos in self.restoreDic, "Cannot call set() twice on same phoneme while re-specifying 'old'"
            assert len(val) <= len(old), "New phoneme is too long!"
            self.restoreDic[phPos] = old
        else: assert phPos in self.restoreDic, "Must specify old values (for restore) when setting for first time"
        self.dFile.seek(phPos)
        self.dFile.write(val+chr(0))
    def __del__(self):
        "WARNING - this might not be called before exit - best to call close() manually"
        if not self.voice or not self.voice in MacBritish_System_Lexicon.instances: return # close() already called, or error in the c'tor
        self.close()
    def close(self):
        for phPos,val in self.restoreDic.items():
            self.set(phPos,val)
        self.dFile.close()
        del MacBritish_System_Lexicon.instances[self.voice]
        assert not os.system("rm -f /tmp/"+self.voice+".PCMWave.lock")
        if self.restoreDic: sys.stderr.write("... lexicon for '"+self.voice+"' restored to normal\n")

if __name__ == "__main__": sys.exit(main())
