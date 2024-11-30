# import re
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.stem.snowball import SnowballStemmer
# import nltk
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# def summarize(text):
#     # Process text by removing numbers and unrecognized punctuation
#     processedText = re.sub("’", "'", text)
#     processedText = re.sub("[^a-zA-Z' ]+", " ", processedText)
#     stopWords = {"needn't", 'be', 'his', 'all', 'under', 'which', "haven't", 'won', 'you', "couldn't", 'then', 'between', 'having', 'll', 'yourselves', 'or', 'down', 'don', 'theirs', 's', 'what', 'because', 'am', 'their', 'against', "it's", 'my', 'why', 'had', 'couldn', 'your', 'was', 'here', 'with', 'out', 'should', 'about', 'them', 'too', 'been', "you've", 'most', 'ain', "you'd", 'm', 'before', "hadn't", 'needn', 'other', 'doesn', 'very', 'are', "mustn't", 'that', 'ours', 'didn', 'mightn', "didn't", 'i', 'but', 'is', 'in', 'to', 'such', 'so', 'no', "aren't", 'into', 'when', 'will', 'wouldn', 'if', 'own', "you'll", 'who', 'aren', 'have', 'we', 'by', 'where', 'during', 'its', 'now', 'than', "weren't", 'she', 'and', 'below', 'being', 'ourselves', 'haven', 'can', 'both', 'they', 'he', 'doing', 'only', 'herself', 'itself', 'each', 'hadn', 'weren', 'isn', "mightn't", 'more', 'shouldn', 'how', 'nor', "you're", 'were', 'from', "should've", 'of', 'wasn', 'a', 'her', 'until', 'him', 'hers', 'again', 'o', "isn't", 'those', 'yourself', "hasn't", "wouldn't", 'hasn', 't', 'any', 'shan', 'this', "she's", 'just', 'yours', 'the', 'd', 'few', 've', 'an', 'further', 'myself', "that'll", 'for', "shouldn't", 'above', 'whom', 'not', 'same', 'does', 'y', 'it', 're', 'through', 'while', 'after', "doesn't", 'mustn', "won't", 'some', 'once', 'himself', 'at', 'as', 'our', 'over', "don't", "shan't", 'has', 'do', 'ma', 'on', 'these', 'did', 'there', 'off', 'me', 'up', 'themselves', "wasn't"}


#     words = word_tokenize(processedText)

#     # Normalize words with Porter stemming and build word frequency table
#     stemmer = SnowballStemmer("english", ignore_stopwords=True)
#     freqTable = dict()
#     for word in words:
#         word = word.lower()
#         if word in stopWords:
#             continue
#         elif stemmer.stem(word) in freqTable:
#             freqTable[stemmer.stem(word)] += 1
#         else:
#             freqTable[stemmer.stem(word)] = 1

#     # Normalize every sentence in the text
#     sentences = sent_tokenize(text)
#     stemmedSentences = []
#     sentenceValue = dict()
#     for sentence in sentences:
#         stemmedSentence = []
#         for word in sentence.lower().split():
#             stemmedSentence.append(stemmer.stem(word))
#         stemmedSentences.append(stemmedSentence)

#     # Calculate value of every normalized sentence based on word frequency table
#     # [:12] helps to save space
#     for num in range(len(stemmedSentences)):
#         for wordValue in freqTable:
#             if wordValue in stemmedSentences[num]:
#                 if sentences[num][:12] in sentenceValue:
#                     sentenceValue[sentences[num][:12]] += freqTable.get(wordValue)
#                 else:
#                     sentenceValue[sentences[num][:12]] = freqTable.get(wordValue)

#     # Determine average value of a sentence in the text
#     sumValues = 0
#     for sentence in sentenceValue:
#         sumValues += sentenceValue.get(sentence)

#     average = int(sumValues / len(sentenceValue))

#     # Create summary of text using sentences that exceed the average value by some factor
#     # This factor can be adjusted to reduce/expand the length of the summary
#     summary = ""
#     for sentence in sentences:
#             if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (3.0 * average):
#                 summary += " " + " ".join(sentence.split())

#     # Process the text in summary and write it to a new file
#     summary = re.sub("’", "'", summary)
#     summary = re.sub("[^a-zA-Z0-9'\"():;,.!?— ]+", " ", summary)
#     return summary




# data = """
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 001 Universit y of R hode I sland
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 002 DigitalComm ons@UR I
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 003 Senior H onor s Projects Honor s Program at the U niversity of R hode I sland
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 004 2011
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 005 Love: A B iolog ical, Psycholog ical and P hilosophic al
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 006 Study
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 007 Heather M . Chapman
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 008 heather_ch apman@m y.uri.edu
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 009 Creative Common s License
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 010 This work i s licensed unde r aCreative Common s Attribution-N oncomme rcial-Share Alike 3.0 L icense.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 011 Follow thi s and a dditional w orks at:http://d igitalcommon s.uri.edu/s rhonor sprog
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 012 Part of the Biology Common s,Philosophy Common s, and the Psychology Common s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 013 This Article i s brought to you for f ree and ope n access by the H onor s Program at the U niversity of R hode I sland a t Di gitalCommon s@UR I. It has be en
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 014 accepted for inclusion in S enior H onor s Projects b y an author ized admini strator of Di gitalCommon s@UR I. For mor e infor mation, p lease contact
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 015 digitalcommon s@e tal.uri.edu.Recomme nded Citation
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 016 Chapman, H eather M., "Love: A B iological, Psychological a nd P hilosophical S tudy " (2011). Senior Honors Projects.Paper 254.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 017 http://d igitalcommon s.uri.edu/s rhonor sprog/254 http://d igitalcommon s.uri.edu/s rhonor sprog/2541
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 018 Running head: LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 019
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 020
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 021
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 022
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 023
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 024
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 025
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 026 Love: A biological, psychological and philosophical study.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 027 Heather Chapman
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 028 University of Rhode Island
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 029
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 030
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 031
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 032
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 033
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 034
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 035
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 036
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 037  2
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 038 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 039 Dedication
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 040
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 041
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 042
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 043 This paper is dedicated to the love of my life
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 044
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 045 Jason Matthew Nye
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 046 October 4,1973 - January 26, 2011
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 047
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 048
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 049
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 050
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 051
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 052
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 053
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 054
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 055
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 056
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 057
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 058
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 059
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 060
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 061  3
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 062 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 063 Abstract
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 064   The concept of love has been an eternally elusive subject.  It is a definition and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 065 meaning that philosophers, psychologists, and biologists have been seeking since the be ginning
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 066 of time.  Wars have been waged and fought over it, while friendships have been initiat ed and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 067 have ended because of this idea.  But what exactly is  love, and why is it important to define this
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 068 enigma?
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 069  In order to help define this idea of love, several books and numerous research article s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 070 were consulted, and interviews were conducted with faculty of The University of R hode Island.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 071 Dr. Nasser Zawia was interviewed, in order to help understand the role of neurobiolog y in the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 072 process of falling in love.  Dr. Zawia explained the importance of neurotransm itters and brain
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 073 activity when a person is in love.  Dr. Dianne Kinsey was consulted, in order to help cl arify the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 074 importance of the psychology of love.  Finally, an interview with Dr. William Kri eger revealed
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 075 the importance of the study of philosophy and how it relates to the concept of love.

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 076  Research has concluded that the disciplines of biology, psychology, and philosophy are

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 077 all important in analyzing love; however, more research needs to be done in order to defin e what
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 078 love actually is, and how we can apply this knowledge in our everyday lives.  With the divor ce
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 079 rates increasing, and the idea of marriage changing in today’s society, th e importance of studying
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 080 the concept of love cannot be overlooked.  It is in this research that we, as a community , will be
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 081 able to understand love, and its importance to the survival of the human race.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 082
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 083
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 084  4
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 085 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 086 Introduction: Why study love?
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 087  The concept of love has been studied throughout history.  Philosophers have been asking
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 088 such questions as “What is love?” and “Why do we love?” since the beginning of time.  Today,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 089 these questions are still being asked, perhaps in a more desperate way.  When childre n are very
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 090 young, they are read fairy tales about Prince Charming rescuing a hel pless princess, with the two
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 091 of them riding off into the sunset to live the seemingly “happily ever after”.  H owever, the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 092 “happily ever after” is never fully described.  Do the prince and the princess get  married, have
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 093 children, and grow old together?  Or do they in fact get married, have children, and then f all out
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 094 of “love” and end up divorced within a few years?  Do they stay happily and passionately i n
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 095 love, or do they stay together only out of the fear of loneliness?  While the rates  do seem to be
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 096 leveling out, the trend remains that a high number of all marriages do ultimately end i n divorce.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 097 The Americans for Divorce Reform currently estimates that "Probably, 40  or possibly even 50
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 098 percent of marriages will end in divorce if current trends continue."  The questi on then becomes
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 099 not only “What is love?”, but “What is love, and why are some people able to stay togethe r,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 100 while other relationships fall apart?”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 101  In order to answer these questions, the concept of love must be examined at differ ent

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 102 angles.  Is it possible that love is just a biological response?  Do people stay toget her because
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 103 their brains have been conditioned to respond to the hormones released?  Or could it possibly  be
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 104 a psychological need and desire to stay together?  Perhaps, couples become “used to” e ach other,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 105 and, afraid of and unable to adapt to change and the uncertainty that comes with that  change,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 106 they stay married?  Finally, could it be the “essence” of love, the idea or co ncept of being in love
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 107 that makes people want to try to work at staying together? 5
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 108 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 109  This paper will examine the biological, psychological and philosophical aspects of  love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 110 For the purpose of this research, partners and couples will be heterosexual; however, hom osexual
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 111 love is equally valuable and important.  The word “marriage” will refer to the union of a  man
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 112 and a woman, and the study of divorce will include couples comprised of a man and a woman.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 113 Research for this paper includes several books, articles and interviews with dif ferent members of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 114 the academic community at the University of Rhode Island.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 115
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 116 Biology: Blame it on the Neurotransmitters
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 117  When a couple meets for the first time, the attraction can be instantaneous.  They  may
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 118 describe the meeting as “a shock to the system”, or “electric”.  When intervi ewed, the men may
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 119 say “Everything else in the room faded, all I could see was her.”  The woman m ay say “I looked
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 120 around the room, and when we locked eyes, I realized I couldn’t take my eyes off of him .”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 121 Could this be love at first sight?  Or is this merely a biological response? I n fact, research does
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 122 find that a person’s eyes do change when they see something they desire.  “Looking i nto a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 123 lover’s eyes is like looking into a fire…Thanks to a shot of adrenaline, your palms sw eat, your
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 124 breathing gets shallow, your skin feels hot, and your pupils dilate.  Your amygdala, th e center of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 125 the brain that processes emotion, blazes with activity. At the same time you pr oduce dopamine, a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 126 ‘feel good’ neurotransmitter that is associated with passion and addiction, and oxy tocin, a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 127 hormone related to bonding.”  (Pincott, 4).  With all of these processes occurring at once , it’s not
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 128 surprising to learn that one’s pupils actually dilate when focusing on an object of de sire.  In fact,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 129 a person’s eyes dilate in order to grasp more of the image of the person.  There m ay also be an
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 130 evolutionary reason that men are attracted to women with larger pupils. “Men pref er big, gaping 6
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 131 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 132 pupils because they’re a sign of arousal and receptivity…big pupils are cues of youth, fertility,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 133 and receptivity- in the subconscious male mind, a sight to behold.” (Pincott, 8).
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 134  In order to understand the brain’s response to love, one must examine the brain and fully
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 135 comprehend the myriad array of structures involved.  One of the main structures involved wi th
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 136 falling in love is the limbic system.  The particular system is well known as being the part of the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 137 brain involved in emotional response.  The limbic system is actually several str uctures combined,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 138 including the basal nuclei, the thalamus, and the hypothalamus.  While all of these struc tures are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 139 vital, the hypothalamus is directly involved in both behavioral and sexual function.  Combining
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 140 these two important functions, one can see how the limbic system is so crucial to f alling in love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 141  Research has concluded, without a doubt that a person responds with their entire body
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 142 when they feel desire.  As stated earlier, when one is around an object of their desi re, adrenaline
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 143 is released, at least in the early stages.  Adrenaline, also known as epinephr ine, which is both a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 144 neurotransmitter and hormone, is released from the adrenal medulla during the  “fight or flight
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 145 response.”  (Sherwood, 188). This response, activated by the body’s sympathetic nervous

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 146 system, prepares the body for the decision to either fight the stressor, or “fl ight”, to run away
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 147 from the attack.  During this reaction, the person’s heart rate increases, the pupils dilate, the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 148 sweat glands are stimulated, and the brain becomes increasingly more aler t.  This reaction, the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 149 sweating, the dilated pupils, the increased heart rate, is exactly how people describe the feeling
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 150 and energy of being “in love”.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 151  In addition to epinephrine, there are several other chemical responses relea sed when a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 152 person experiences “love at first sight.”  Endorphins, oxytocin, dopamine, and vasopressin a re
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 153 also important to examine when looking at the brain’s response to love.  Endorphins are pept ides
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 154 that are manufactured in the pituitary gland and the hypothalamus.  These “fe el good chemicals” 7
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 155 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 156 act both as an analgesic and as a sedative.  Endorphins are released during exe rcise, which is
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 157 what many avid runners describe as a “runner’s high”.  Eventually, the runner’s body  begins to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 158 crave the release of endorphins, which is why many exercise enthusiasts r eport the “need” to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 159 exercise.  Endorphins are also released during sex; they provide the “feel-good, cal ming” effect
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 160 that one feels immediately after orgasm.  Finally, endorphins are released t hrough touch, which
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 161 is why a mother’s touch can soothe a crying infant.  “Endorphins, for instance, can cre ate the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 162 sensation of euphoria and relief from pain.” (Selhub, 33).  It is that compelling euphori c feeling
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 163 that couples describe when they say they have “fallen in love.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 164  In her book, A Natural History of Love , author Diane Ackerman discusses the importance
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 165 of the hormone oxytocin in a person’s experience of love.  Oxytocin, also known as the “cuddle
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 166 chemical”, “plays an important role in romantic love, as a hormone that encourage s cuddling
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 167 between lovers and increases pleasure during lovemaking…The hormone stimulates the  smooth
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 168 muscles and sensitizes the nerves, and snowballs during sexual arousal.” (Ackerm an, 163).
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 169 Oxytocin is also linked to the feeling of “closeness” that one experiences af ter intercourse, which
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 170 may explain why women are statistically more likely to “fall” for  a man that they may know they
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 171 have no future with, yet they mistakenly associate the feeling they experi ence after the release of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 172 oxytocin with love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 173  Since oxytocin is released through physical touch, including “stroking, cuddling,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 174 hugging, kissing, or having sex” (Pincott, 144), it can be concluded that it is also associa ted with
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 175 the release of other distinct hormones in the body.  In fact, “oxytocin works in t andem with other
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 176 neurotransmitters such as testosterone…oxytocin may also influence how the  feel-good
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 177 neurotransmitters dopamine and norepinepherine hit the reward parts of the brain.” (Pincott,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 178 145).  When this various cornucopia of hormones and neurotransmitters are released, the body  8
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 179 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 180 can associate this feeling with love.  This is why one may become “attached”  to a partner that is
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 181 absolutely not  a good match.  Even if one consciously knows that the other person is a bad fit,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 182 this cascade of neurotransmitters may confuse the brain into believing the m atch is compatible.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 183 Unfortunately (or fortunately from an evolutionary standpoint), the relationship eventua lly ends.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 184 However, hormones are also extremely important in the feeling of addiction, dopami ne
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 185 especially.  Perhaps it is this feeling of “addiction” that keeps couples toge ther.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 186  Women like to cuddle after intercourse, while men just want to sleep.  This is a we ll-
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 187 known “fact” that is commonly shared by society.  But, interestingly, there i s actually a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 188 biological reason for this desire.  “Women experience stronger effects of ox ytocin than men
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 189 because women have more estrogen, and estrogen makes oxytocin receptors more  sensitive.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 190 (Pincott, 146).  At least now there is a biological explanation for that fact.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 191  Dopamine, a monoamine neurotransmitter, plays an essential role in attraction.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 192 Dopamine plays several different roles in the body, including “being involved in fi ne muscle
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 193 movement, integration of emotions and thoughts, involved in decision making, and stimulating
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 194 the hypothalamus to release hormones (sex, thyroid, adrenal).” (Varcarolis &  Halter, 50).  One
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 195 can see that, with both the involvement of emotion and thoughts, and stimulating the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 196 hypothalamus to release hormones, biologically speaking, dopamine is crucial to f alling in love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 197 Interestingly, a decrease in dopamine has been associated with both Parkinson’s di sease and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 198 depression, whereas an increase in dopamine is associated with schizophrenia and mani a.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 199  Considering the contrast in medical conditions that can be associated with dopami ne
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 200 (mania versus depression), it can be concluded that the release, or perhaps lack ther eof,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 201 dopamine in a person’s brain can be affiliated with how they act when they are ei ther in love, or
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 202 conversely, suffering from the loss of a love.  Indeed, when one first “falls in l ove”, as 9
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 203 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 204 mentioned earlier, their actions can become erratic.  They want to spend every w aking moment
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 205 with the object of their affection; they pine for their presence when they are apart.  Once one has
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 206 experienced heartbreak, it can often be difficult to just get out of bed to face each day .  Life can
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 207 lose meaning, anhedonia (lack of finding pleasure in activities that one once enjoy ed) is a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 208 symptom commonly described by those experiencing separation and divorce.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 209  This contrast can easily be explained when one examines dopamine’s other role i n the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 210 brain, which is that of addiction.  In the August, 2010 issue of the Harvard Mental Heal th Letter,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 211 researchers found that “All addictive substances (and many pleasurable act ivities) release the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 212 neurotransmitter dopamine in the nucleus accumbens, a cluster of nerve cells lyi ng deep in the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 213 brain. Initially researchers thought that dopamine acted as a hedonic signal—one  that registers
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 214 pleasure in the brain—and that this signal prompted people to continue seeking the substanc e.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 215 In this way, combining biology with psychology for the moment, one can conclude that being
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 216 with a partner whose actions are associated with the release of dopamine in one’ s brain, can
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 217 actually lead to a physical “addiction” to the person.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 218  Finally, vasopressin plays an important chemical role in one’s ability to fall  in love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 219 Vasopressin, also known as antidiuretic hormone (ADH), is a hormone that serves m any
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 220 functions in the human body.  It controls the reabsorption process in the kidneys, plays a role  in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 221 maintaining homeostasis, and helps to restore blood pressure in cases such as hypovole mic
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 222 shock.  However, for the purpose of this study, it is important to note that when vasopressin i s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 223 released, it can, in fact, help men bond with their mates.  “One brain study found that peopl e in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 224 relationships for more than two years show increased activity in the rewar d area of the ventral
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 225 pallidum, which is rich with vasopressin receptors.” (Pincott, 304)   10
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 226 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 227   In addition to the brain’s response to the neurotransmitters and other “love” chemic als
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 228 being released, there is also another very important aspect of chemistry tha t is responsible for the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 229 feeling of attraction.  Pheromones are chemical signals that are release d by the body that can
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 230 serve to attract or repel potential mates.  While there is currently some c ontroversy pertaining to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 231 the determination of what pheromones actually do in the body, there is no controversy over t he
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 232 fact that they do exist.  For years, researchers have been aware of the pr esence of a vomeronasal
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 233 organ (VNO) in mammals, however “only recently have scientist discovered re al evidence of a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 234 VNO in human adults.” (Pincott, 28).  It is also hypothesized that “Pheromones could trigger  our
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 235 sex drive by traveling the neural pathway that connects the nose to the hypothalam us, a region of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 236 the brain that initiates the release of sex hormones and fuels erotic feeling s and sensations.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 237 (Pincott, 29)  Knowing that pheromones do exist, and their purpose, it can be accurately
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 238 concluded that people fall in love with the “scent” of a person.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 239  There is a very distinct scent that each body gives off, however it is not neces sarily
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 240 consciously noted.  Of course, as the human race has evolved, so have the litany of groomi ng
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 241 habits.  People now bathe frequently, use scented soaps, buy perfume or cologne, all i n the hopes
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 242 to make themselves more attractive to their potential mates.  However, it is i nteresting to note
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 243 that, while one may drench themselves with all of the cologne in the world, if a potenti al mate
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 244 isn’t attracted to the person’s pheromones, there isn’t much chance of love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 245  Interestingly, one’s immune system plays a very important role in pheromones  and their
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 246 role in attraction.  When one thinks of love, one doesn’t often think of the immune system.  The
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 247 immune system is in place to protect the body from illness, to fight against forei gn particle
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 248 invaders, to help heal a cut, and to maintain homeostasis in the body.  However, it does so much
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 249 more than just those key actions.  “Researchers believe that one major source of huma n 11
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 250 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 251 pheromones is the immune system’s major histocompatibility complex (MHC). Whet her you’re
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 252 attracted to or repulsed by a man’s body odor may depend strongly on your respective i mmune
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 253 systems.” (Pincott, 29).  It is in this way that, biologically speaking; one picks  the “best” mate.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 254 One very important, albeit subconscious, way of making sure that one’s offspring has the best
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 255 chance of survival is by picking a partner whose MHC is dramatically differ ent from one’s own.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 256 “If you have children with a [partner] whose MHC variants are most unlike your ow n, your kids
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 257 may inherit a more diverse MHC and stronger immune system that identify and de stroy a greater
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 258 range of bacteria and viruses. If your partner has MHC genes that are ve ry similar to your own,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 259 your children might not be as healthy.” (Pincott, 32). Biologically speaking, love s eemingly
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 260 depends on your MHC.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 261  By choosing this variant MHC, it has been concluded that the offspring will be more
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 262 advanced immunologically than if the MHC was similar.  However, knowing what pheromone s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 263 are, and knowing that they are detected on such an unconscious level, how does one actuall y
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 264 detect this MHC?  “Researchers speculate that MHC genes code for specif ic proteins that
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 265 circulate in the bloodstream.  These proteins bind to odorants in concentrations that depends on a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 266 person’s MHC. These…ooze out of sweat glands in the armpits and the genital area s.” (Pincott,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 267 32).  This leads one to conclude that cuddling allows not only oxytocin to be released, but the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 268 detection of pheromones as well.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 269  Interestingly, women who are on hormonal contraceptives may actually choos e partners
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 270 whose MHC is actually similar to theirs.  “Researchers are unsure why the Pill reverses women’s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 271 usual preference for men with MHC-dissimilar genes, but it’s evident that i t has something to do
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 272 with the lack of hormonal fluctuations.” (Pincott, 34).  This can end up being a problem,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 273 especially if the woman has been on a hormonal contraceptive throughout dating and, 12
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 274 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 275 subsequently, marriage.  If the couple decides that they want to have children, and the wom an
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 276 stops taking the contraception, the couple may find that, unfortunately, they are not att racted to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 277 each other any longer.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 278  While neurotransmitters do play an enormous part in the brain’s role in falling in love ,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 279 there are structures of the brain itself that change when a person is in love.  A study  done by
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 280 Helen Fisher, Lucy Brown and Arthur Aron demonstrated this change.  In this stud y, couples
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 281 who described themselves as “intensely in love” were recruited, and while they were looking at a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 282 picture of their beloved, their brains were scanned by an fMRI. “The researche rs saw a glow in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 283 several regions of the lovers’ brains, representing blood flow. Among them were thr ee important
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 284 clusters of brain cells related to motivation and reward…the right ventral tegm ental area (VTA),
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 285 the medial caudate nucleus, and the nucleus accumbens.” (Pincott, 283)  These parts of the br ain
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 286 are known as the reward centers.  When these areas are activated, the person “f eels good”, which
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 287 is due to the fact that dopamine is being released by the VTA to the caudate nucle us and the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 288 nucleus accumbens.  As previously discussed, dopamine is the “feel good” chemical.  Being in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 289 love causes dopamine to be released and makes one feel good, which then causes the person to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 290 spend more time with their mate.  The more time couples spend together in the early s tages of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 291 the relationship, the more the neurotransmitters are subsequently released.  The  more
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 292 neurotransmitters that are released, the more the couples want to spend time tog ether.  This is an
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 293 ever-repeating cycle, which leads to an “addiction”.  And, as previously stated, dopam ine plays a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 294 very important role in addiction.  This idea of reward/punishment will be discussed furt her in the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 295 following section.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 296  An interview with Dr. Nasser Zawia, explored the concept of biology and love.  Dr.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 297 Zawia states that we “fall in love with the brain”.  This is contrary to the idea  that the media 13
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 298 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 299 places on love, where men are shown commercials of scantily clad women, and women a re
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 300 shown commercials of shirtless, muscular construction workers.  These media im ages are what
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 301 we, as a society, are told we are supposed to find attractive.  However, the previous r esearch has
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 302 proven Dr. Zawia is correct; humans do in fact fall in love with their brains.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 303  Dr. Zawia also concluded that pheromones do play an important role in falling in love .
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 304 He describes the VNO and its role in detecting pheromones.  Dr. Zawia states “ if you like
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 305 someone’s smell, you want to be with them.”  This is exactly what previous rese arch has found,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 306 that a person’s scent is staggeringly important in attraction.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 307  In addition to the biology of love, Dr. Zawia discussed the importance of the role of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 308 psychology in relationships.  He stated that “a person is like an addictive drug.”  While  the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 309 importance of dopamine and addiction has already been discussed, Dr. Zawia explores  this idea
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 310 further, by stating “there is a reward/punishment area of the brain responsibl e for people staying
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 311 together.”  The reward/punishment concept will be discussed later in the psycholog y section of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 312 this research paper.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 313  When Dr. Zawia was asked which aspect of love played the greatest role in love , he
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 314 stated “In the beginning, the most important part is biology, then, as love matures, psy chology
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 315 becomes the most important.”  He also stated that “love is the most important emot ion for
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 316 people.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 317
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 318 Psychology: Love as a form of hysteria
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 319  While the biological components of love have been demonstrated as being extremely
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 320 important, one must examine the psychology of love in order to get a full picture of thi s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 321 important human experience.  While love can seem like an extremely abstract conce pt, it was 14
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 322 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 323 important and concrete enough for psychologists to study, and eventually, several theo ries on
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 324 love have consequently evolved.  One cannot discuss the psychology of love without discussing
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 325 one of psychology’s forefathers, Sigmund Freud.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 326  Freud (May 6 1856 –September 23 1939) was an Austrian neurologist, and is considered
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 327 the father of psychoanalysis. Freud had a great deal of theories for pretty m uch everything
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 328 conceivable, from dreams and their meanings, to love and hysteria.  “His many cont ributions to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 329 knowledge include his studies of the development of the sexual instinct in children, his
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 330 descriptions of the workings of the unconscious mind and of the nature of repression, and his
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 331 examinations and interpretations of dreams.” (Drabble & Stringer, 2003).  He was a lso an
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 332 advocate for the use of cocaine, and even wrote a paper on the benefits of using the drug .
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 333  Freud believed that love and sexuality were extremely intertwined, and beg inning at a

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 334 very young age, one experiences these feelings, although they are often misguided.  Freud
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 335 believed in and coined the phrases “Oedipus complex” and “Electra complex”.  In Fr eud’s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 336 scientific opinion, young boys are sexually attracted to their mothers, and wa nt to kill their
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 337 fathers in order to have their mothers all to themselves.  Not to be outdone, young girls  desire
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 338 their fathers, and want to eliminate their mothers, in order to be with their fat hers.  These ideas
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 339 (Oedipus and Electra respectively) provide motivation for the children, and when the c hildren are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 340 spurned by their parents, they seek out others for their love and affection.  Of course, thi s idea
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 341 brought forth a great deal of controversy for Freud, as it is often disturbing to thi nk of children as
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 342 sexual creatures, and society’s view of incest is that it is absolutely unnat ural.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 343  Taking the information we know from Freud, we can then conclude that we, as adults, are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 344 constantly searching for that partner that reminds us of our mother or father.  “W omen’s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 345 tendency to marry men who resemble Dad, if Dad is loving, adds to the increasing evidenc e that 15
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 346 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 347 women lean toward the familiar and the positive for long-term relationships…We may  be
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 348 modeling our marriage on Mom’s, or unconsciously deciding that since Dad is a good parent,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 349 than a man who looks like him will be too.” (Pincott, 21).  This idea may be disturbing for some
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 350 people; however Pincott also concludes “the attraction is limited to general res emblances.” (21).
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 351  Now that the relationship between childhood associations of love, and how we pick a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 352 mate (whether this belief is true or not is still up for debate), one can examine, f rom a Freudian
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 353 perspective, how this love transfers to adult behavior.  In order to further exami ne this theory, we
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 354 must create a hypothetical situation to examine from a Freudian perspecti ve.  Imagine a couple,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 355 having been together for several years, having yet another fight over who’s  turn it is to take out
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 356 the garbage.  If this couple has not learned how to communicate effectively, there m ight be name
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 357 calling, temper tantrums thrown, or the fight could escalate to encompass issues  that have
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 358 nothing to do with taking out the garbage.  What would cause a pair of grown adults to act in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 359 such a childish way?  “Freud concludes that when lovers act irrationally what t hey’re really
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 360 doing is regressing to the needs, insecurities, and obsessions of childhood.” (Ackerma n, 134).
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 361 Everyone is guilty of behaving in an immature way, at one point or another, but it was F reud
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 362 who realized the impetus for these actions.  Of course, Freud did have a lot of people tryi ng to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 363 disprove his theories (in fact, there are some that denounce his work altogether), howe ver, one
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 364 cannot disprove his enormous impact in the field of psychology.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 365  Another important psychologist involved in the psychology of love was Abraham
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 366 Maslow.  Maslow (1908-1970) was considered the father of humanistic psychology.  Humanisti c
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 367 theory is one that focuses on “human potential and free will to choose life patterns  that are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 368 supportive of personal growth. Humanistic frameworks emphasize a person’s capaci ty for self-
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 369 actualization.” (Varcarolis, 38).  In fact, no psychology class is complete wi thout studying 16
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 370 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 371 Maslow’s hierarchy of needs.  This theory includes the idea that “humans are ac tive rather than
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 372 passive participants in life, striving for self-actualization.” (Varcar olis, 38).  Contrary to Freud’s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 373 theory, an adult can actively make choices in their lives, as opposed to most of their a ctions
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 374 being mainly subconscious.  Maslow’s hierarchy is pyramid shaped, with the most fundam ental
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 375 needs at the bottom, and the “more distinctly human needs” placed on the top.  The categorie s,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 376 from bottom to top, include physiological needs, safety needs, love and belonging needs, e steem,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 377 self-actualization, and self-transcendence.  Physiological needs include food, water, and rest.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 378 Safety needs include security, protection, stability, and structure.  Love and be longing needs
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 379 include affectionate relationships and adoration. Esteem includes both self-este em, and esteem
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 380 from others. Self-actualization is defined as “becoming everything one is c apable of.”

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 381 (Varcarolis, 39).  Finally, self-transcendence is exceeding beyond one’s ow n limitations.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 382  When one views the hierarchy, it is not difficult to understand how his theory is so
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 383 crucial to the idea of love.  When one’s physiological needs are covered, the next st ep is safety
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 384 requirements.  While this does include physical safety, it also includes stabil ity, structure, and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 385 order.  This is one reason that many couples do not want to divorce, mainly because this ver y
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 386 idea will be shaken to the core.  How often do women say “I’d love to leave him, but I have  to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 387 take care of the children.” Or, if the woman did not achieve adequate education and has no wor k
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 388 experience, she may feel stuck in the relationship, as she cannot adequately provide s tability and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 389 security for herself.  Safety experts often tell women who live alone to have a m ale friend record
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 390 the outgoing message on the answering machine, to place a pair of men’s shoes by  the door, and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 391 to hang a man’s jacket on the coat rack, in case a burglar is casing the house.  Unfort unately, in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 392 today’s society, a woman alone is seen as helpless.  In fact, to take it one st ep further, women are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 393 often told, when they go to a party, to say “we” often, in case a potential criminal i s mingling 17
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 394 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 395 among the partygoers.  These ideas, while definitely smart, just show how vulnerabl e a single
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 396 woman can be in today’s society.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 397  On a brighter note, the security from being in a couple can reinforce the feeli ng of love,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 398 because it protects one from desolation and loneliness.  There are so many articl es that are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 399 published, especially around the holiday season, on how to survive being single.  Since the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 400 security from being in a couple is there, those in love do not have to worry about how society
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 401 will view them.  They can often enjoy the holidays more, knowing they have someone to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 402 celebrate with, and in fact, commercials absolutely prey on this feeling.  The ps ychology of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 403 commercials and the impact on the media is too complex to explain in this one paper, but  there
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 404 are a few points that are necessary to highlight.  There is a certain jewe lry company that has a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 405 particular commercial, which airs during each holiday season (especially C hristmas and

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 406 Valentine’s Day.)  In this commercial, a woman is sitting in a rocking chai r with her child.  The
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 407 husband (presumably) comes up to her with a box in his hand, containing jewelry of some sort.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 408 The next shot is that of the woman accepting the jewelry, and gazing at her hus band with love,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 409 while he looks at her in adoration.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 410  Psychologically speaking, this commercial plays perfectly into Maslow’ s hierarchy of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 411 needs.  The woman’s physiological needs are being met (she is resting comfor tably with her
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 412 infant), she is feeling safe and secure, and her love and belonging needs are being  met.  She feels
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 413 the love from her husband, and both her husband and her infant give her a sense of belonging in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 414 the family.  This is not necessarily a bad commercial; it is just one exam ple of Maslow’s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 415 hierarchy being portrayed in the media.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 416  Every human being wants to be loved.  This is not a wholly incomprehensible statement.

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 417 With the exception of some people with personality disorders, everyone wants to be loved.  T he 18
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 418 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 419 feeling that one experiences, especially when they know that they are loved, i s indescribable.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 420 This is why love is a significant component in Maslow’s hierarchy.  “People have a need for
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 421 intimate relationships, love, affection, and belonging and will seek to overcome fee lings of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 422 aloneness and alienation. Maslow stresses the importance of having a famil y and a home and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 423 being part of identifiable groups.” (Varcarolis, 39).  It is this idea, this need for love that keeps us
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 424 searching for, and then staying with, our partners.  As stated earlier, 40-50%  of marriages are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 425 ending in divorce; however, this statistic does not take into account the marriages that  are staying
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 426 together for “convenience”.  A marriage of convenience can include marriage for mon etary
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 427 gains, an exchange of services, or, heartbreakingly, a marriage that stays t ogether because the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 428 people involved are afraid of being alone and the thought of unending loneliness.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 429  Feeling alone can be one of the supremely devastating feelings in the worl d.  Oftentimes,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 430 for couples who have been together for years, when one spouse dies, the remaining spouse oft en
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 431 joins them in death.  This may be because both partners were old, however, it can also be
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 432 attributed to the feeling that one just cannot live without their love.  It’s alm ost a beautiful thing
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 433 to think about, to love someone so strongly that you just cannot imagine one’s existence or  life
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 434 without them.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 435  Shakespeare touched on this subject when he wrote the play Romeo and Juliet .  While the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 436 two lovers, Romeo and Juliet, definitely were not together for a long time, their love  for each
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 437 other was beyond measure.  Through a number of misunderstandings, Romeo comes across
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 438 Juliet’s (supposedly) lifeless body, and declares himself unable to live without he r.  “For fear of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 439 that I still will stay with thee and never from this pallet of dim night depart  again. Here, here I
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 440 will remain with worms that are thy chambermaids, O, here will I set up my  everlasting rest…O
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 441 true apothecary! Thy drugs are quick. Thus, with a kiss I die.”  (152). Upon waking fr om her 19
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 442 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 443 slumber, Juliet finds Romeo dead next to her.  Unable to live without him, she grabs Romeo’s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 444 dagger and declares “O happy dagger! This is thy sheath; there rust, and let m e die.” (154).
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 445 While this is, of course, a dramatization of the idea of not being able to live without y our partner,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 446 it does show that this idea of belonging together has been together for generations.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 447  In addition to Freud’s view on love being developed during childhood and Maslow’s idea

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 448 that love is important enough to be included in the hierarchy of needs, there is another as pect of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 449 psychology that drives couples to stay together.  B.F. Skinner (1904-1990) was a beha vioral
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 450 theorist who is perhaps best known for his theory of operant conditioning.  “Operant
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 451 conditioning, in which voluntary behaviors are learned through consequences, and behavioral
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 452 responses are elicited through reinforcement, which causes a behavior to occur more  frequently.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 453 (Varcarolis, 32).  This idea of operant conditioning can accurately be applied to the i dea of love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 454   Operant conditioning is most associated with the reward/punishment concept.  The
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 455 reward can come in the form of either positive reinforcement (such as receiving  a trophy for
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 456 finishing first in a marathon) or negative reinforcement (opening an umbrella on a  rainy day, in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 457 order to not get wet).  Contrary to popular belief, negative reinforcement is not a puni shment; it
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 458 is a removal of an unwanted stimulus.  In contrast to reinforcement is that of punishm ent, such as
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 459 being arrested after driving while intoxicated.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 460   Love is the ultimate positive reinforcement.  Historically, courting rit uals, which are the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 461 path to love, are essentially working on the same idea as Skinner’s positive reinfor cement.  For
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 462 example, when a man is smitten with a woman, he will often send flowers, call oft en, write love
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 463 letters, and take the woman out on elaborate dates.  In return, the woman recognizes  that he has
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 464 potential as a provider, which in turn makes her more affectionate towards him.  He r ecognizes
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 465 this affection as being a positive reward, and in turn, will continue his pursuit and the  behavior.   20
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 466 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 467  As mentioned earlier, the hormones and neurotransmitters involved in falling in love a lso
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 468 play a role in the reward/punishment aspect of love.  When one is in love, there is often a n
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 469 increase in the amount of touching involved, whether it be hugging, kissing or cuddling.  This
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 470 touch releases the endorphins, dopamine, oxytocin, etc., which produces a feeling of euphor ia
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 471 and contentment.  One then desires this feeling, so they spend more time with their love d one,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 472 which releases more of the hormones/neurotransmitters.  This is a consistent cy cle of positive
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 473 reinforcement.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 474  In an interview with Dianne Kinsey, the concept of the psychology of love was dis cussed.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 475 When asked why people stay together, Ms. Kinsey stated that it was due to a “f ear of loneliness.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 476 This fear of loneliness keeps couples together, even when it might be best for all pa rties to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 477 ultimately separate.  In addition, Ms. Kinsey stated “there is a deep fear  of growing old alone.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 478 This fear will keep couples together; in fact, it can even be the motivation to have chi ldren.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 479 While the desire to have children can absolutely be a biologically driven need, the tr uth is that
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 480 some couples have children so there will be someone to take care of them when they ge t older.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 481  When the idea of loneliness is discussed further, Ms. Kinsey stated that marr iage can be a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 482 “convenience” and that “divorce takes too much effort.”  In order to combat this loneli ness that
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 483 couples feel when they are in a relationship without love, they often resort to extr amarital affairs.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 484 These affairs can bring back the feelings of excitement and “newness” i nto a person’s seemingly
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 485 empty life.  Unfortunately, the adulterer may not realize that these affa irs will not fix the inherent
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 486 problem, which is that the marriage is failing.  Ultimately, the excitement  of the affair will wear
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 487 off, and the adulterer will have to either face the truth, or continue living with the deni al.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 488  Ms. Kinsey also discussed the fact that there are different types of love. She  stated that
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 489 the most important type of love in her opinion is “agape”, which is a spiritual love. Ms. K insey 21
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 490 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 491 stated that this is when people place the “wellbeing of others above their own.”  This i dea of love
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 492 is different from the love that one thinks of normally; however it is equally beautif ul and vitally
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 493 important.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 494  The concept of divorce was also discussed, and when Ms. Kinsey was asked why it
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 495 seems that divorce is so prevalent in today’s society, she stated “there is n o longer a stigma
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 496 around divorce…today’s culture has supported children who come from divorced homes.”  This
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 497 is certainly true, however women today who become divorced do not face the same stigma a s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 498 they did in the 1950’s.  Since the women’s liberation movement, women now have many more
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 499 choices, and are able to sustain themselves and their children, if need be.  Unfortunat ely, women
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 500 still do not make a salary equal to a man’s, yet this gap is closing.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 501  When asked which personality aspects a person must have in order to make their
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 502 relationship work, Ms. Kinsey stated they need to be “flexible to change, and they n eed to be
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 503 resilient.”  These personality traits are especially important in maki ng a marriage endure.  For
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 504 example, if a couple gets married at the age of twenty-five, they are not going to be the same
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 505 people when they are thirty or even forty.  Life will change them, they may go t hrough career
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 506 changes, have children, or take up new hobbies.  In order for the relationship to survive, sust ain
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 507 and grow, the people involved need to be willing to evolve with it.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 508  When asked which aspect of love, biology, psychology, or philosophy, is the most
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 509 important in a successful relationship; Ms. Kinsey stated that it is “a com bination of all three.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 510 She stated “love is the most powerful force in the entire world, but we have to start w ith
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 511 ourselves.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 512
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 513 Philosophy: The Essence of Love 22
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 514 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 515  Throughout this paper, all the books read, all the interviews conducted, one concept
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 516 continually emerged, and that is “loving is part of the human condition.”  We are inhere ntly
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 517 programmed to love, whether it’s biologically, psychologically, or by some other m echanism we
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 518 have yet to understand.  “Contrary to what philosophers, moralists, theoreticians, in- laws, and
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 519 counselors have always argued, love is not a choice. It is a biological imperat ive. And just as
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 520 evolution favored human beings who were able to stand upright, it favored human beings who
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 521 felt love. It favored them because love has great survival value.” (Acker man, 151).   But what is
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 522 this love, why are we driven to achieve it, and why are we so despondent when it’s miss ing from
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 523 our lives?  In order to understand and answer these questions, it is imperative to tra vel through
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 524 history, and to discuss how love was understood in the past.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 525  In ancient Greece, Athens was considered the “birthplace of western philosophy .”  The

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 526 family was not as we know it to be today.  “…the family was not one household in Athens; it
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 527 was the city itself, whose affairs all men knew and played a role in…Once le gitimate heirs were
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 528 born to a man, things loosened up slightly for the wives, who could then divorce to get out of a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 529 particularly nasty marriage.” (Ackerman, 23).  While there were, unquestionabl y, extramarital
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 530 affairs, they were more well-known and accepted in that society.  There is  a similarity in one
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 531 aspect, however. “It’s not that Athenian women didn’t sometimes have premarita l or extramarital
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 532 affairs, but those who did were thought shocking and immoral.” (Ackerman, 23).  This idea  is
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 533 still true in today’s society, men’s affairs are almost accepted, and a t the very least, they aren’t
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 534 seen to be as much of a scandal of that of women’s affairs.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 535  With the knowledge of extramarital affairs and divorce, one may wonder if the anc ient

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 536 Greeks believed in love.  In fact, the belief that society holds today, that there i s one person out
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 537 there for everyone, a “soul mate”, actually originated with Plato.  Plato (429 –347 B.C.E.) 23
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 538 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 539 discussed the idea of the soul being separate from the body. “We must recogni ze that the soul is
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 540 a different sort of object from the body — so much so that it does not depend on the existence of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 541 the body for its functioning, and can in fact grasp the nature of the forms far more e asily when it
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 542 is not encumbered by its attachment to anything corporea.” (Kraut, 2009).  In additi on, “the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 543 preconceived image of the person we are meant to love comes from Plato, who said t hat there are
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 544 perfect universal forms, and humans are constantly searching for facsimil es of those forms.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 545 (Ackerman, 126).  Plato’s idea, that there is someone out there for everyone, is what kee ps
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 546 everyone searching for adoration and love.  We, as a society, are taught, from the very

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 547 beginning, that love is real, our soul mates are out there, and, ultimately, we will fi nd the one
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 548 who makes us complete and whole.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 549  Perhaps couples stay together because of Plato’s idea of “soul mates”. When coupl es get
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 550 married, those who are religious feel that they have found their soul mates, and t hey make a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 551 solemn promise to God to make the marriage work and flourish.  In getting a divorce, the couple
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 552 not only has to admit defeat to themselves, but also break a promise to God.  They have to admi t
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 553 that the person they married may not be their “soul mate”, and that can be terrifyi ng, because
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 554 they need to go back out into the world of dating.  Some of them may have the faith that they
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 555 will find their love, others may meet and fall in love with someone else who may not be r ight for
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 556 them.  All of this work is done in search of a “soul mate”.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 557  A more modern philosopher, Michael Boylan, discusses his idea of love in his book The
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 558 Good, The True and The Beautiful . He states that love is an action, and the concept leads us to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 559 change and grow as human beings.  “Love is a powerful motivator for being good. The  affective
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 560 part of the good will is no poor sister to the rational. It can be an effective gui de to good action.”  24
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 561 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 562 (27).  One can conclude, then, that the essence of love is not only to find your soul mate, but it
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 563 also allows one to be “good”.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 564  Finally, one must philosophically compare love and sex, since these two ideas have  a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 565 biological and psychological basis.  Another modern philosopher, Robert Rowland Smith, does
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 566 just that in his book Breakfast with Socrates .  He concludes that “According to biblical tradition
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 567 love can, in turn, be subdivided into friendship (philia) and spiritual or emotional love (agape) ,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 568 which complicates the relationship with sex, or eros, a bit further.” (198). This the ory, a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 569 complication of love and sex, is one that has been discussed for generations.  Harlan E llison once
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 570 concluded that “Love ain't nothing but sex misspelled.” While this quote is often la ughed off,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 571 there is some truth to the saying.  Love and sex are absolutely entangled; howe ver it is possible
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 572 to have one without the other.  But that’s a story, and a lesson, for another day.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 573  In an interview with William Krieger, the philosophical aspect of love wa s discussed.

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 574 Dr. Krieger stated that “psychology started from philosophy”, and that both of the se disciplines
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 575 are entangled.  Considering the research that was done based on Plato and Socrates’  work, it’s
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 576 not difficult to see how these two disciplines play off and complement one another.  When asked
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 577 what he thought was the reason couples are able to stay together, Dr. Krieger st ated it was due to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 578 “a person’s ability to change.”  When asked to clarify on that idea, Dr. Kriege r stated “people
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 579 change radically over time; the couples have to be able to change as well.”  This  idea is similar to
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 580 Ms. Kinsey’s, that in order for a marriage to survive, a person has to be able to chang e, to be
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 581 flexible and resilient.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 582  Dr. Krieger also agreed with Ms. Kinsey’s idea that there is less of a stigm a surrounding
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 583 divorce in today’s society.  He stated that “years ago, women had no opportunities…eve n less if
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 584 you had kids.”  In addition to the stigma surrounding divorce being lessened, Dr. Krieger  also 25
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 585 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 586 stated that there is less stigma surrounding the concept of seeking therapy.  Couples are now able
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 587 to feel more free to visit a therapist in order to work through their difficulties , and in this way,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 588 they are able to potentially save some marriages that would have ended in di vorce.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 589  Dr. Krieger also concurs with Dr. Zawia and Ms. Kinsey, insofar as he believe s that love
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 590 and successful marriages are due to a combination of biology, psychology and philosophical
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 591 aspects.  He stated that “neurochemistry is definitely important, but it’s not al l of it.”  Dr. Krieger
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 592 states that he absolutely believes in love and marriage, and that it is important to w ork together
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 593 and change with the relationship in order to make it successful.  He concludes that “L ife is too
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 594 short to be terribly miserable.”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 595
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 596 Biology, Psychology, Philosophy: Who wins?
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 597   After researching all three areas of love, it is difficult to say which o f them is the most
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 598 important when it comes to love, marriage, and success in a relationship.  Biologic al factors,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 599 such as the release of the hormones and neurotransmitters, are absolutely import ant in falling in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 600 love, and staying in love.  Evolutionarily speaking, pheromones are also extremely impor tant in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 601 finding the best mate, especially if one wants to have children and give them the best  chance of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 602 survival, thanks to the MHC.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 603  Psychological aspects, such as Freud’s ideas of the way one picks their mate  based on

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 604 their relationship with their parents, and also their regression into irrational be havior when in
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 605 love, is also equally important.  The fact that Maslow has both the ideas of “safety  and security”
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 606 and “love and belonging” in his hierarchy is important, because it allows one to recog nize that
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 607 love isn’t just a random concept, it is necessary for good mental health.  Skinner’s ex planation of 26
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 608 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 609 the positive reinforcement involved in operant conditioning allows us insight in how psycholog y
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 610 explains and reinforces love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 611  Finally, Plato’s discussion of the idea of a “soul mate” is crucial to today’ s idea of love.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 612 We spend a considerable amount of time searching for our soul mates; some of us spend our
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 613 entire lives, just to feel the type of love that Plato described. Michael Boy lan’s idea that love is a
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 614 means towards doing ‘good’ can be seen everywhere.  A person may donate an organ or bone
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 615 marrow to a loved one.  We help our loved ones work through issues that would be ignored if
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 616 they were a stranger.  The idea that love is an impetus for good embodies the esse nce of the
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 617 human spirit.  Finally, Robert Rowland Smith’s idea of love and sex being intertwined brin gs
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 618 new meaning to sex, turning it from a biological drive to something beautiful share d by humans,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 619 in order to feel closer to one another.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 620  In conclusion, more research needs to be done in order to discover what love truly is.

# hdfs://localhost:9000/user/joy/input/love.pdf # Line 621 While the previous research is extremely beneficial in helping to define love, c ase studies of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 622 couples who have been married for a substantial amount of time (greater than twent y-five years)
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 623 would be helpful in order to come to a more definite conclusion.  While no final definition of
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 624 love has been concluded, a quote from Pascal comes the closest to gleaning a clue:  "T he heart
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 625 has reasons that reason cannot know."
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 626
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 627
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 628
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 629
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 630
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 631  27
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 632 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 633 References
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 634
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 635 Ackerman, D. (1994). A natural history of love . New York, NY: Random House, Inc.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 636
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 637 Boylan, M. (2008). The good, the true, and the beautiful.  New York, NY: Continuum
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 638  International Publishing Group.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 639
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 640 Drabble, M., Stringer, J."Freud, Sigmund." The Concise Oxford Companion to English
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 641  Literature . 2003. Retrieved November 29, 2010 from Encyclopedia.com:
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 642  http://www.encyclopedia.com/doc/1O54-FreudSigmund.html
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 643
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 644 Kraut, Richard, "Plato", The Stanford Encyclopedia of Philosophy (Fall 2009 Edition) , Edward
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 645  N. Zalta (ed.), http://plato.stanford.edu/archives/fall2009/entries/plato/.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 646
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 647 Pincott, J. (2008). Do gentlemen really prefer blondes?: Bodies, behavior and brains- The
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 648  science behind sex, love & attraction.  New York, NY: Random House, Inc.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 649
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 650 Selhub, E. (2009). The love response . New York, NY: Random House, Inc.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 651
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 652  Shakespeare, W.(1964). The tragedy of Romeo and Juliet.  Bryant, J.A. (Ed.).  New York, NY.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 653  Signet.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 654  28
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 655 LOVE
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 656 Sherwood, L. (2006). Fundamentals of physiology: A human perspective.  Belmont, CA:
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 657  Thomson Brooks/Cole
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 658
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 659 "Sigmund Freud." The Columbia Encyclopedia, Sixth Edition . 2008. Retrieved November 29,
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 660  2010 from Encyclopedia.com: http://www.encyclopedia.com/doc/1E1-Freud-Si.html
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 661
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 662 Smith, R.R. (2009). Breakfast with Socrates . New York, NY: Simon & Schuster, Inc.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 663
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 664 Varcarolis, E.M. & Halter, M.J. (2010). Foundations of psychiatric mental health nursing: A
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 665  clinical approach.  St. Louis: Elsevier, Inc.
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 666
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 667
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 668
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 669
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 670
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 671
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 672
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 673
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 674
# hdfs://localhost:9000/user/joy/input/love.pdf # Line 675
# """

# lines = data.strip().split("\n")

# # Extract filename, line number, and content
# parsed_lines = []
# pattern = re.compile(r"(hdfs://.+?\.pdf)\s+# Line (\d+)(.*)")

# for line in lines:
#     match = pattern.match(line)
#     if match:
#         filename = match.group(1)
#         line_number = int(match.group(2))
#         content = match.group(3).strip()
#         parsed_lines.append((filename, line_number, content))

# # Sort by filename and line number
# parsed_lines.sort(key=lambda x: (x[0], x[1]))

# # Concatenate content by filename
# file_content_dict = {}

# for filename, _, content in parsed_lines:
#     if filename not in file_content_dict:
#         file_content_dict[filename] = content
#     else:
#         file_content_dict[filename] += (" " + content) if content else ""

# # Output the concatenated result
# for filename, content in file_content_dict.items():
#     summary = summarize(content)
#     file_content_dict[filename] = summary
# print(file_content_dict)




import time

start = time.time()
with open("aa.txt", 'wb') as file:
    file.write(b"hello")
end=time.time()
print(end-start)