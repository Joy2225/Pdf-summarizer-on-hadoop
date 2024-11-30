#!/usr/bin/env python3

import sys
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
a='''../tests\love.pdf	Universit y of R hode I sland
DigitalComm ons@UR I
Senior H onor s Projects Honor s Program at the U niversity of R hode I sland
2011
Love: A B iolog ical, Psycholog ical and P hilosophic al
Study
Heather M . Chapman
heather_ch apman@m y.uri.edu
Creative Common s License
This work i s licensed unde r aCreative Common s Attribution-N oncomme rcial-Share Alike 3.0 L icense.
Follow thi s and a dditional w orks at:http://d igitalcommon s.uri.edu/s rhonor sprog
Part of the Biology Common s,Philosophy Common s, and the Psychology Common s
This Article i s brought to you for f ree and ope n access by the H onor s Program at the U niversity of R hode I sland a t Di gitalCommon s@UR I. It has be en
accepted for inclusion in S enior H onor s Projects b y an author ized admini strator of Di gitalCommon s@UR I. For mor e infor mation, p lease contact
digitalcommon s@e tal.uri.edu.Recomme nded Citation
Chapman, H eather M., "Love: A B iological, Psychological a nd P hilosophical S tudy " (2011). Senior Honors Projects.Paper 254.
http://d igitalcommon s.uri.edu/s rhonor sprog/254 http://d igitalcommon s.uri.edu/s rhonor sprog/2541 
Running head: LOVE 
 
 
 
 
 
 
 
Love: A biological, psychological and philosophical study. 
Heather Chapman 
University of Rhode Island 
 
 
 
 
 
 
 
 
 2 
LOVE 
Dedication 
 
 
 
This paper is dedicated to the love of my life 
 
Jason Matthew Nye 
October 4,1973 - January 26, 2011 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 3 
LOVE 
Abstract 
  The concept of love has been an eternally elusive subject.  It is a definition and 
meaning that philosophers, psychologists, and biologists have been seeking since the be ginning 
of time.  Wars have been waged and fought over it, while friendships have been initiat ed and 
have ended because of this idea.  But what exactly is  love, and why is it important to define this 
enigma?  
 In order to help define this idea of love, several books and numerous research article s 
were consulted, and interviews were conducted with faculty of The University of R hode Island.  
Dr. Nasser Zawia was interviewed, in order to help understand the role of neurobiolog y in the 
process of falling in love.  Dr. Zawia explained the importance of neurotransm itters and brain 
activity when a person is in love.  Dr. Dianne Kinsey was consulted, in order to help cl arify the 
importance of the psychology of love.  Finally, an interview with Dr. William Kri eger revealed 
the importance of the study of philosophy and how it relates to the concept of love.    
 Research has concluded that the disciplines of biology, psychology, and philosophy are  
all important in analyzing love; however, more research needs to be done in order to defin e what 
love actually is, and how we can apply this knowledge in our everyday lives.  With the divor ce 
rates increasing, and the idea of marriage changing in today’s society, th e importance of studying 
the concept of love cannot be overlooked.  It is in this research that we, as a community , will be 
able to understand love, and its importance to the survival of the human race.    
 
 
 4 
LOVE 
Introduction: Why study love? 
 The concept of love has been studied throughout history.  Philosophers have been asking 
such questions as “What is love?” and “Why do we love?” since the beginning of time.  Today, 
these questions are still being asked, perhaps in a more desperate way.  When childre n are very 
young, they are read fairy tales about Prince Charming rescuing a hel pless princess, with the two 
of them riding off into the sunset to live the seemingly “happily ever after”.  H owever, the 
“happily ever after” is never fully described.  Do the prince and the princess get  married, have 
children, and grow old together?  Or do they in fact get married, have children, and then f all out 
of “love” and end up divorced within a few years?  Do they stay happily and passionately i n 
love, or do they stay together only out of the fear of loneliness?  While the rates  do seem to be 
leveling out, the trend remains that a high number of all marriages do ultimately end i n divorce.  
The Americans for Divorce Reform currently estimates that "Probably, 40  or possibly even 50 
percent of marriages will end in divorce if current trends continue."  The questi on then becomes 
not only “What is love?”, but “What is love, and why are some people able to stay togethe r, 
while other relationships fall apart?” 
 In order to answer these questions, the concept of love must be examined at differ ent 
angles.  Is it possible that love is just a biological response?  Do people stay toget her because 
their brains have been conditioned to respond to the hormones released?  Or could it possibly  be 
a psychological need and desire to stay together?  Perhaps, couples become “used to” e ach other, 
and, afraid of and unable to adapt to change and the uncertainty that comes with that  change, 
they stay married?  Finally, could it be the “essence” of love, the idea or co ncept of being in love 
that makes people want to try to work at staying together? 5 
LOVE 
 This paper will examine the biological, psychological and philosophical aspects of  love.  
For the purpose of this research, partners and couples will be heterosexual; however, hom osexual 
love is equally valuable and important.  The word “marriage” will refer to the union of a  man 
and a woman, and the study of divorce will include couples comprised of a man and a woman.  
Research for this paper includes several books, articles and interviews with dif ferent members of 
the academic community at the University of Rhode Island.   
 
Biology: Blame it on the Neurotransmitters 
 When a couple meets for the first time, the attraction can be instantaneous.  They  may 
describe the meeting as “a shock to the system”, or “electric”.  When intervi ewed, the men may 
say “Everything else in the room faded, all I could see was her.”  The woman m ay say “I looked 
around the room, and when we locked eyes, I realized I couldn’t take my eyes off of him .”  
Could this be love at first sight?  Or is this merely a biological response? I n fact, research does 
find that a person’s eyes do change when they see something they desire.  “Looking i nto a 
lover’s eyes is like looking into a fire…Thanks to a shot of adrenaline, your palms sw eat, your 
breathing gets shallow, your skin feels hot, and your pupils dilate.  Your amygdala, th e center of 
the brain that processes emotion, blazes with activity. At the same time you pr oduce dopamine, a 
‘feel good’ neurotransmitter that is associated with passion and addiction, and oxy tocin, a 
hormone related to bonding.”  (Pincott, 4).  With all of these processes occurring at once , it’s not 
surprising to learn that one’s pupils actually dilate when focusing on an object of de sire.  In fact, 
a person’s eyes dilate in order to grasp more of the image of the person.  There m ay also be an 
evolutionary reason that men are attracted to women with larger pupils. “Men pref er big, gaping 6 
LOVE 
pupils because they’re a sign of arousal and receptivity…big pupils are cues of youth, fertility, 
and receptivity- in the subconscious male mind, a sight to behold.” (Pincott, 8).   
 In order to understand the brain’s response to love, one must examine the brain and fully 
comprehend the myriad array of structures involved.  One of the main structures involved wi th 
falling in love is the limbic system.  The particular system is well known as being the part of the 
brain involved in emotional response.  The limbic system is actually several str uctures combined, 
including the basal nuclei, the thalamus, and the hypothalamus.  While all of these struc tures are 
vital, the hypothalamus is directly involved in both behavioral and sexual function.  Combining 
these two important functions, one can see how the limbic system is so crucial to f alling in love. 
 Research has concluded, without a doubt that a person responds with their entire body 
when they feel desire.  As stated earlier, when one is around an object of their desi re, adrenaline 
is released, at least in the early stages.  Adrenaline, also known as epinephr ine, which is both a 
neurotransmitter and hormone, is released from the adrenal medulla during the  “fight or flight 
response.”  (Sherwood, 188). This response, activated by the body’s sympathetic nervous 
system, prepares the body for the decision to either fight the stressor, or “fl ight”, to run away 
from the attack.  During this reaction, the person’s heart rate increases, the pupils dilate, the 
sweat glands are stimulated, and the brain becomes increasingly more aler t.  This reaction, the 
sweating, the dilated pupils, the increased heart rate, is exactly how people describe the feeling 
and energy of being “in love”.   
 In addition to epinephrine, there are several other chemical responses relea sed when a 
person experiences “love at first sight.”  Endorphins, oxytocin, dopamine, and vasopressin a re 
also important to examine when looking at the brain’s response to love.  Endorphins are pept ides 
that are manufactured in the pituitary gland and the hypothalamus.  These “fe el good chemicals” 7 
LOVE 
act both as an analgesic and as a sedative.  Endorphins are released during exe rcise, which is 
what many avid runners describe as a “runner’s high”.  Eventually, the runner’s body  begins to 
crave the release of endorphins, which is why many exercise enthusiasts r eport the “need” to 
exercise.  Endorphins are also released during sex; they provide the “feel-good, cal ming” effect 
that one feels immediately after orgasm.  Finally, endorphins are released t hrough touch, which 
is why a mother’s touch can soothe a crying infant.  “Endorphins, for instance, can cre ate the 
sensation of euphoria and relief from pain.” (Selhub, 33).  It is that compelling euphori c feeling 
that couples describe when they say they have “fallen in love.”  
 In her book, A Natural History of Love , author Diane Ackerman discusses the importance 
of the hormone oxytocin in a person’s experience of love.  Oxytocin, also known as the “cuddle  
chemical”, “plays an important role in romantic love, as a hormone that encourage s cuddling 
between lovers and increases pleasure during lovemaking…The hormone stimulates the  smooth 
muscles and sensitizes the nerves, and snowballs during sexual arousal.” (Ackerm an, 163).  
Oxytocin is also linked to the feeling of “closeness” that one experiences af ter intercourse, which 
may explain why women are statistically more likely to “fall” for  a man that they may know they 
have no future with, yet they mistakenly associate the feeling they experi ence after the release of 
oxytocin with love.   
 Since oxytocin is released through physical touch, including “stroking, cuddling, 
hugging, kissing, or having sex” (Pincott, 144), it can be concluded that it is also associa ted with 
the release of other distinct hormones in the body.  In fact, “oxytocin works in t andem with other 
neurotransmitters such as testosterone…oxytocin may also influence how the  feel-good 
neurotransmitters dopamine and norepinepherine hit the reward parts of the brain.” (Pincott, 
145).  When this various cornucopia of hormones and neurotransmitters are released, the body  8 
LOVE 
can associate this feeling with love.  This is why one may become “attached”  to a partner that is 
absolutely not  a good match.  Even if one consciously knows that the other person is a bad fit, 
this cascade of neurotransmitters may confuse the brain into believing the m atch is compatible.  
Unfortunately (or fortunately from an evolutionary standpoint), the relationship eventua lly ends.  
However, hormones are also extremely important in the feeling of addiction, dopami ne 
especially.  Perhaps it is this feeling of “addiction” that keeps couples toge ther.  
 Women like to cuddle after intercourse, while men just want to sleep.  This is a we ll-
known “fact” that is commonly shared by society.  But, interestingly, there i s actually a 
biological reason for this desire.  “Women experience stronger effects of ox ytocin than men 
because women have more estrogen, and estrogen makes oxytocin receptors more  sensitive.” 
(Pincott, 146).  At least now there is a biological explanation for that fact. 
 Dopamine, a monoamine neurotransmitter, plays an essential role in attraction.  
Dopamine plays several different roles in the body, including “being involved in fi ne muscle 
movement, integration of emotions and thoughts, involved in decision making, and stimulating 
the hypothalamus to release hormones (sex, thyroid, adrenal).” (Varcarolis &  Halter, 50).  One 
can see that, with both the involvement of emotion and thoughts, and stimulating the 
hypothalamus to release hormones, biologically speaking, dopamine is crucial to f alling in love.  
Interestingly, a decrease in dopamine has been associated with both Parkinson’s di sease and 
depression, whereas an increase in dopamine is associated with schizophrenia and mani a.   
 Considering the contrast in medical conditions that can be associated with dopami ne 
(mania versus depression), it can be concluded that the release, or perhaps lack ther eof, 
dopamine in a person’s brain can be affiliated with how they act when they are ei ther in love, or 
conversely, suffering from the loss of a love.  Indeed, when one first “falls in l ove”, as 9 
LOVE 
mentioned earlier, their actions can become erratic.  They want to spend every w aking moment 
with the object of their affection; they pine for their presence when they are apart.  Once one has 
experienced heartbreak, it can often be difficult to just get out of bed to face each day .  Life can 
lose meaning, anhedonia (lack of finding pleasure in activities that one once enjoy ed) is a 
symptom commonly described by those experiencing separation and divorce.   
 This contrast can easily be explained when one examines dopamine’s other role i n the 
brain, which is that of addiction.  In the August, 2010 issue of the Harvard Mental Heal th Letter, 
researchers found that “All addictive substances (and many pleasurable act ivities) release the 
neurotransmitter dopamine in the nucleus accumbens, a cluster of nerve cells lyi ng deep in the 
brain. Initially researchers thought that dopamine acted as a hedonic signal—one  that registers 
pleasure in the brain—and that this signal prompted people to continue seeking the substanc e.”  
In this way, combining biology with psychology for the moment, one can conclude that being  
with a partner whose actions are associated with the release of dopamine in one’ s brain, can 
actually lead to a physical “addiction” to the person.   
 Finally, vasopressin plays an important chemical role in one’s ability to fall  in love.  
Vasopressin, also known as antidiuretic hormone (ADH), is a hormone that serves m any 
functions in the human body.  It controls the reabsorption process in the kidneys, plays a role  in 
maintaining homeostasis, and helps to restore blood pressure in cases such as hypovole mic 
shock.  However, for the purpose of this study, it is important to note that when vasopressin i s 
released, it can, in fact, help men bond with their mates.  “One brain study found that peopl e in 
relationships for more than two years show increased activity in the rewar d area of the ventral 
pallidum, which is rich with vasopressin receptors.” (Pincott, 304)   10 
LOVE 
  In addition to the brain’s response to the neurotransmitters and other “love” chemic als 
being released, there is also another very important aspect of chemistry tha t is responsible for the 
feeling of attraction.  Pheromones are chemical signals that are release d by the body that can 
serve to attract or repel potential mates.  While there is currently some c ontroversy pertaining to 
the determination of what pheromones actually do in the body, there is no controversy over t he 
fact that they do exist.  For years, researchers have been aware of the pr esence of a vomeronasal 
organ (VNO) in mammals, however “only recently have scientist discovered re al evidence of a 
VNO in human adults.” (Pincott, 28).  It is also hypothesized that “Pheromones could trigger  our 
sex drive by traveling the neural pathway that connects the nose to the hypothalam us, a region of 
the brain that initiates the release of sex hormones and fuels erotic feeling s and sensations.” 
(Pincott, 29)  Knowing that pheromones do exist, and their purpose, it can be accurately 
concluded that people fall in love with the “scent” of a person.   
 There is a very distinct scent that each body gives off, however it is not neces sarily 
consciously noted.  Of course, as the human race has evolved, so have the litany of groomi ng 
habits.  People now bathe frequently, use scented soaps, buy perfume or cologne, all i n the hopes 
to make themselves more attractive to their potential mates.  However, it is i nteresting to note 
that, while one may drench themselves with all of the cologne in the world, if a potenti al mate 
isn’t attracted to the person’s pheromones, there isn’t much chance of love.   
 Interestingly, one’s immune system plays a very important role in pheromones  and their 
role in attraction.  When one thinks of love, one doesn’t often think of the immune system.  The 
immune system is in place to protect the body from illness, to fight against forei gn particle 
invaders, to help heal a cut, and to maintain homeostasis in the body.  However, it does so much 
more than just those key actions.  “Researchers believe that one major source of huma n 11 
LOVE 
pheromones is the immune system’s major histocompatibility complex (MHC). Whet her you’re 
attracted to or repulsed by a man’s body odor may depend strongly on your respective i mmune 
systems.” (Pincott, 29).  It is in this way that, biologically speaking; one picks  the “best” mate.  
One very important, albeit subconscious, way of making sure that one’s offspring has the best 
chance of survival is by picking a partner whose MHC is dramatically differ ent from one’s own.  
“If you have children with a [partner] whose MHC variants are most unlike your ow n, your kids 
may inherit a more diverse MHC and stronger immune system that identify and de stroy a greater 
range of bacteria and viruses. If your partner has MHC genes that are ve ry similar to your own, 
your children might not be as healthy.” (Pincott, 32). Biologically speaking, love s eemingly 
depends on your MHC. 
 By choosing this variant MHC, it has been concluded that the offspring will be more  
advanced immunologically than if the MHC was similar.  However, knowing what pheromone s 
are, and knowing that they are detected on such an unconscious level, how does one actuall y 
detect this MHC?  “Researchers speculate that MHC genes code for specif ic proteins that 
circulate in the bloodstream.  These proteins bind to odorants in concentrations that depends on a  
person’s MHC. These…ooze out of sweat glands in the armpits and the genital area s.” (Pincott, 
32).  This leads one to conclude that cuddling allows not only oxytocin to be released, but the 
detection of pheromones as well.   
 Interestingly, women who are on hormonal contraceptives may actually choos e partners 
whose MHC is actually similar to theirs.  “Researchers are unsure why the Pill reverses women’s 
usual preference for men with MHC-dissimilar genes, but it’s evident that i t has something to do 
with the lack of hormonal fluctuations.” (Pincott, 34).  This can end up being a problem, 
especially if the woman has been on a hormonal contraceptive throughout dating and, 12 
LOVE 
subsequently, marriage.  If the couple decides that they want to have children, and the wom an 
stops taking the contraception, the couple may find that, unfortunately, they are not att racted to 
each other any longer.   
 While neurotransmitters do play an enormous part in the brain’s role in falling in love , 
there are structures of the brain itself that change when a person is in love.  A study  done by 
Helen Fisher, Lucy Brown and Arthur Aron demonstrated this change.  In this stud y, couples 
who described themselves as “intensely in love” were recruited, and while they were looking at a 
picture of their beloved, their brains were scanned by an fMRI. “The researche rs saw a glow in 
several regions of the lovers’ brains, representing blood flow. Among them were thr ee important 
clusters of brain cells related to motivation and reward…the right ventral tegm ental area (VTA), 
the medial caudate nucleus, and the nucleus accumbens.” (Pincott, 283)  These parts of the br ain 
are known as the reward centers.  When these areas are activated, the person “f eels good”, which 
is due to the fact that dopamine is being released by the VTA to the caudate nucle us and the 
nucleus accumbens.  As previously discussed, dopamine is the “feel good” chemical.  Being in 
love causes dopamine to be released and makes one feel good, which then causes the person to 
spend more time with their mate.  The more time couples spend together in the early s tages of 
the relationship, the more the neurotransmitters are subsequently released.  The  more 
neurotransmitters that are released, the more the couples want to spend time tog ether.  This is an 
ever-repeating cycle, which leads to an “addiction”.  And, as previously stated, dopam ine plays a 
very important role in addiction.  This idea of reward/punishment will be discussed furt her in the 
following section. 
 An interview with Dr. Nasser Zawia, explored the concept of biology and love.  Dr. 
Zawia states that we “fall in love with the brain”.  This is contrary to the idea  that the media 13 
LOVE 
places on love, where men are shown commercials of scantily clad women, and women a re 
shown commercials of shirtless, muscular construction workers.  These media im ages are what 
we, as a society, are told we are supposed to find attractive.  However, the previous r esearch has 
proven Dr. Zawia is correct; humans do in fact fall in love with their brains. 
 Dr. Zawia also concluded that pheromones do play an important role in falling in love .  
He describes the VNO and its role in detecting pheromones.  Dr. Zawia states “ if you like 
someone’s smell, you want to be with them.”  This is exactly what previous rese arch has found, 
that a person’s scent is staggeringly important in attraction.   
 In addition to the biology of love, Dr. Zawia discussed the importance of the role of 
psychology in relationships.  He stated that “a person is like an addictive drug.”  While  the 
importance of dopamine and addiction has already been discussed, Dr. Zawia explores  this idea 
further, by stating “there is a reward/punishment area of the brain responsibl e for people staying 
together.”  The reward/punishment concept will be discussed later in the psycholog y section of 
this research paper. 
 When Dr. Zawia was asked which aspect of love played the greatest role in love , he 
stated “In the beginning, the most important part is biology, then, as love matures, psy chology 
becomes the most important.”  He also stated that “love is the most important emot ion for 
people.”   
 
Psychology: Love as a form of hysteria 
 While the biological components of love have been demonstrated as being extremely  
important, one must examine the psychology of love in order to get a full picture of thi s 
important human experience.  While love can seem like an extremely abstract conce pt, it was 14 
LOVE 
important and concrete enough for psychologists to study, and eventually, several theo ries on 
love have consequently evolved.  One cannot discuss the psychology of love without discussing 
one of psychology’s forefathers, Sigmund Freud. 
 Freud (May 6 1856 –September 23 1939) was an Austrian neurologist, and is considered 
the father of psychoanalysis. Freud had a great deal of theories for pretty m uch everything 
conceivable, from dreams and their meanings, to love and hysteria.  “His many cont ributions to 
knowledge include his studies of the development of the sexual instinct in children, his 
descriptions of the workings of the unconscious mind and of the nature of repression, and his 
examinations and interpretations of dreams.” (Drabble & Stringer, 2003).  He was a lso an 
advocate for the use of cocaine, and even wrote a paper on the benefits of using the drug .   
 Freud believed that love and sexuality were extremely intertwined, and beg inning at a 
very young age, one experiences these feelings, although they are often misguided.  Freud 
believed in and coined the phrases “Oedipus complex” and “Electra complex”.  In Fr eud’s 
scientific opinion, young boys are sexually attracted to their mothers, and wa nt to kill their 
fathers in order to have their mothers all to themselves.  Not to be outdone, young girls  desire 
their fathers, and want to eliminate their mothers, in order to be with their fat hers.  These ideas 
(Oedipus and Electra respectively) provide motivation for the children, and when the c hildren are 
spurned by their parents, they seek out others for their love and affection.  Of course, thi s idea 
brought forth a great deal of controversy for Freud, as it is often disturbing to thi nk of children as 
sexual creatures, and society’s view of incest is that it is absolutely unnat ural.   
 Taking the information we know from Freud, we can then conclude that we, as adults, are  
constantly searching for that partner that reminds us of our mother or father.  “W omen’s 
tendency to marry men who resemble Dad, if Dad is loving, adds to the increasing evidenc e that 15 
LOVE 
women lean toward the familiar and the positive for long-term relationships…We may  be 
modeling our marriage on Mom’s, or unconsciously deciding that since Dad is a good parent, 
than a man who looks like him will be too.” (Pincott, 21).  This idea may be disturbing for some 
people; however Pincott also concludes “the attraction is limited to general res emblances.” (21).   
 Now that the relationship between childhood associations of love, and how we pick a 
mate (whether this belief is true or not is still up for debate), one can examine, f rom a Freudian 
perspective, how this love transfers to adult behavior.  In order to further exami ne this theory, we 
must create a hypothetical situation to examine from a Freudian perspecti ve.  Imagine a couple, 
having been together for several years, having yet another fight over who’s  turn it is to take out 
the garbage.  If this couple has not learned how to communicate effectively, there m ight be name 
calling, temper tantrums thrown, or the fight could escalate to encompass issues  that have 
nothing to do with taking out the garbage.  What would cause a pair of grown adults to act in 
such a childish way?  “Freud concludes that when lovers act irrationally what t hey’re really 
doing is regressing to the needs, insecurities, and obsessions of childhood.” (Ackerma n, 134).  
Everyone is guilty of behaving in an immature way, at one point or another, but it was F reud 
who realized the impetus for these actions.  Of course, Freud did have a lot of people tryi ng to 
disprove his theories (in fact, there are some that denounce his work altogether), howe ver, one 
cannot disprove his enormous impact in the field of psychology. 
 Another important psychologist involved in the psychology of love was Abraham 
Maslow.  Maslow (1908-1970) was considered the father of humanistic psychology.  Humanisti c 
theory is one that focuses on “human potential and free will to choose life patterns  that are 
supportive of personal growth. Humanistic frameworks emphasize a person’s capaci ty for self-
actualization.” (Varcarolis, 38).  In fact, no psychology class is complete wi thout studying 16 
LOVE 
Maslow’s hierarchy of needs.  This theory includes the idea that “humans are ac tive rather than 
passive participants in life, striving for self-actualization.” (Varcar olis, 38).  Contrary to Freud’s 
theory, an adult can actively make choices in their lives, as opposed to most of their a ctions 
being mainly subconscious.  Maslow’s hierarchy is pyramid shaped, with the most fundam ental 
needs at the bottom, and the “more distinctly human needs” placed on the top.  The categorie s, 
from bottom to top, include physiological needs, safety needs, love and belonging needs, e steem, 
self-actualization, and self-transcendence.  Physiological needs include food, water, and rest.  
Safety needs include security, protection, stability, and structure.  Love and be longing needs 
include affectionate relationships and adoration. Esteem includes both self-este em, and esteem 
from others. Self-actualization is defined as “becoming everything one is c apable of.” 
(Varcarolis, 39).  Finally, self-transcendence is exceeding beyond one’s ow n limitations.  
 When one views the hierarchy, it is not difficult to understand how his theory is so 
crucial to the idea of love.  When one’s physiological needs are covered, the next st ep is safety 
requirements.  While this does include physical safety, it also includes stabil ity, structure, and 
order.  This is one reason that many couples do not want to divorce, mainly because this ver y 
idea will be shaken to the core.  How often do women say “I’d love to leave him, but I have  to 
take care of the children.” Or, if the woman did not achieve adequate education and has no wor k 
experience, she may feel stuck in the relationship, as she cannot adequately provide s tability and 
security for herself.  Safety experts often tell women who live alone to have a m ale friend record 
the outgoing message on the answering machine, to place a pair of men’s shoes by  the door, and 
to hang a man’s jacket on the coat rack, in case a burglar is casing the house.  Unfort unately, in 
today’s society, a woman alone is seen as helpless.  In fact, to take it one st ep further, women are 
often told, when they go to a party, to say “we” often, in case a potential criminal i s mingling 17 
LOVE 
among the partygoers.  These ideas, while definitely smart, just show how vulnerabl e a single 
woman can be in today’s society. 
 On a brighter note, the security from being in a couple can reinforce the feeli ng of love, 
because it protects one from desolation and loneliness.  There are so many articl es that are 
published, especially around the holiday season, on how to survive being single.  Since the 
security from being in a couple is there, those in love do not have to worry about how society 
will view them.  They can often enjoy the holidays more, knowing they have someone to 
celebrate with, and in fact, commercials absolutely prey on this feeling.  The ps ychology of 
commercials and the impact on the media is too complex to explain in this one paper, but  there 
are a few points that are necessary to highlight.  There is a certain jewe lry company that has a 
particular commercial, which airs during each holiday season (especially C hristmas and 
Valentine’s Day.)  In this commercial, a woman is sitting in a rocking chai r with her child.  The 
husband (presumably) comes up to her with a box in his hand, containing jewelry of some sort.  
The next shot is that of the woman accepting the jewelry, and gazing at her hus band with love, 
while he looks at her in adoration.   
 Psychologically speaking, this commercial plays perfectly into Maslow’ s hierarchy of 
needs.  The woman’s physiological needs are being met (she is resting comfor tably with her 
infant), she is feeling safe and secure, and her love and belonging needs are being  met.  She feels 
the love from her husband, and both her husband and her infant give her a sense of belonging in 
the family.  This is not necessarily a bad commercial; it is just one exam ple of Maslow’s 
hierarchy being portrayed in the media. 
 Every human being wants to be loved.  This is not a wholly incomprehensible statement.  
With the exception of some people with personality disorders, everyone wants to be loved.  T he 18 
LOVE 
feeling that one experiences, especially when they know that they are loved, i s indescribable.  
This is why love is a significant component in Maslow’s hierarchy.  “People have a need for 
intimate relationships, love, affection, and belonging and will seek to overcome fee lings of 
aloneness and alienation. Maslow stresses the importance of having a famil y and a home and 
being part of identifiable groups.” (Varcarolis, 39).  It is this idea, this need for love that keeps us 
searching for, and then staying with, our partners.  As stated earlier, 40-50%  of marriages are 
ending in divorce; however, this statistic does not take into account the marriages that  are staying 
together for “convenience”.  A marriage of convenience can include marriage for mon etary 
gains, an exchange of services, or, heartbreakingly, a marriage that stays t ogether because the 
people involved are afraid of being alone and the thought of unending loneliness. 
 Feeling alone can be one of the supremely devastating feelings in the worl d.  Oftentimes, 
for couples who have been together for years, when one spouse dies, the remaining spouse oft en 
joins them in death.  This may be because both partners were old, however, it can also be 
attributed to the feeling that one just cannot live without their love.  It’s alm ost a beautiful thing 
to think about, to love someone so strongly that you just cannot imagine one’s existence or  life 
without them.   
 Shakespeare touched on this subject when he wrote the play Romeo and Juliet .  While the 
two lovers, Romeo and Juliet, definitely were not together for a long time, their love  for each 
other was beyond measure.  Through a number of misunderstandings, Romeo comes across 
Juliet’s (supposedly) lifeless body, and declares himself unable to live without he r.  “For fear of 
that I still will stay with thee and never from this pallet of dim night depart  again. Here, here I 
will remain with worms that are thy chambermaids, O, here will I set up my  everlasting rest…O 
true apothecary! Thy drugs are quick. Thus, with a kiss I die.”  (152). Upon waking fr om her 19 
LOVE 
slumber, Juliet finds Romeo dead next to her.  Unable to live without him, she grabs Romeo’s 
dagger and declares “O happy dagger! This is thy sheath; there rust, and let m e die.” (154). 
While this is, of course, a dramatization of the idea of not being able to live without y our partner, 
it does show that this idea of belonging together has been together for generations.  
 In addition to Freud’s view on love being developed during childhood and Maslow’s idea 
that love is important enough to be included in the hierarchy of needs, there is another as pect of 
psychology that drives couples to stay together.  B.F. Skinner (1904-1990) was a beha vioral 
theorist who is perhaps best known for his theory of operant conditioning.  “Operant 
conditioning, in which voluntary behaviors are learned through consequences, and behavioral  
responses are elicited through reinforcement, which causes a behavior to occur more  frequently.” 
(Varcarolis, 32).  This idea of operant conditioning can accurately be applied to the i dea of love.   
  Operant conditioning is most associated with the reward/punishment concept.  The 
reward can come in the form of either positive reinforcement (such as receiving  a trophy for 
finishing first in a marathon) or negative reinforcement (opening an umbrella on a  rainy day, in 
order to not get wet).  Contrary to popular belief, negative reinforcement is not a puni shment; it 
is a removal of an unwanted stimulus.  In contrast to reinforcement is that of punishm ent, such as 
being arrested after driving while intoxicated.  
  Love is the ultimate positive reinforcement.  Historically, courting rit uals, which are the 
path to love, are essentially working on the same idea as Skinner’s positive reinfor cement.  For 
example, when a man is smitten with a woman, he will often send flowers, call oft en, write love 
letters, and take the woman out on elaborate dates.  In return, the woman recognizes  that he has 
potential as a provider, which in turn makes her more affectionate towards him.  He r ecognizes 
this affection as being a positive reward, and in turn, will continue his pursuit and the  behavior.   20 
LOVE 
 As mentioned earlier, the hormones and neurotransmitters involved in falling in love a lso 
play a role in the reward/punishment aspect of love.  When one is in love, there is often a n 
increase in the amount of touching involved, whether it be hugging, kissing or cuddling.  This 
touch releases the endorphins, dopamine, oxytocin, etc., which produces a feeling of euphor ia 
and contentment.  One then desires this feeling, so they spend more time with their love d one, 
which releases more of the hormones/neurotransmitters.  This is a consistent cy cle of positive 
reinforcement.   
 In an interview with Dianne Kinsey, the concept of the psychology of love was dis cussed.  
When asked why people stay together, Ms. Kinsey stated that it was due to a “f ear of loneliness.”  
This fear of loneliness keeps couples together, even when it might be best for all pa rties to 
ultimately separate.  In addition, Ms. Kinsey stated “there is a deep fear  of growing old alone.”  
This fear will keep couples together; in fact, it can even be the motivation to have chi ldren.  
While the desire to have children can absolutely be a biologically driven need, the tr uth is that 
some couples have children so there will be someone to take care of them when they ge t older.   
 When the idea of loneliness is discussed further, Ms. Kinsey stated that marr iage can be a 
“convenience” and that “divorce takes too much effort.”  In order to combat this loneli ness that 
couples feel when they are in a relationship without love, they often resort to extr amarital affairs.  
These affairs can bring back the feelings of excitement and “newness” i nto a person’s seemingly 
empty life.  Unfortunately, the adulterer may not realize that these affa irs will not fix the inherent 
problem, which is that the marriage is failing.  Ultimately, the excitement  of the affair will wear 
off, and the adulterer will have to either face the truth, or continue living with the deni al. 
 Ms. Kinsey also discussed the fact that there are different types of love. She  stated that 
the most important type of love in her opinion is “agape”, which is a spiritual love. Ms. K insey 21 
LOVE 
stated that this is when people place the “wellbeing of others above their own.”  This i dea of love 
is different from the love that one thinks of normally; however it is equally beautif ul and vitally 
important. 
 The concept of divorce was also discussed, and when Ms. Kinsey was asked why it 
seems that divorce is so prevalent in today’s society, she stated “there is n o longer a stigma 
around divorce…today’s culture has supported children who come from divorced homes.”  This 
is certainly true, however women today who become divorced do not face the same stigma a s 
they did in the 1950’s.  Since the women’s liberation movement, women now have many more 
choices, and are able to sustain themselves and their children, if need be.  Unfortunat ely, women 
still do not make a salary equal to a man’s, yet this gap is closing.   
 When asked which personality aspects a person must have in order to make their 
relationship work, Ms. Kinsey stated they need to be “flexible to change, and they n eed to be 
resilient.”  These personality traits are especially important in maki ng a marriage endure.  For 
example, if a couple gets married at the age of twenty-five, they are not going to be the same 
people when they are thirty or even forty.  Life will change them, they may go t hrough career 
changes, have children, or take up new hobbies.  In order for the relationship to survive, sust ain 
and grow, the people involved need to be willing to evolve with it. 
 When asked which aspect of love, biology, psychology, or philosophy, is the most 
important in a successful relationship; Ms. Kinsey stated that it is “a com bination of all three.”  
She stated “love is the most powerful force in the entire world, but we have to start w ith 
ourselves.”  
  
Philosophy: The Essence of Love 22 
LOVE 
 Throughout this paper, all the books read, all the interviews conducted, one concept 
continually emerged, and that is “loving is part of the human condition.”  We are inhere ntly 
programmed to love, whether it’s biologically, psychologically, or by some other m echanism we 
have yet to understand.  “Contrary to what philosophers, moralists, theoreticians, in- laws, and 
counselors have always argued, love is not a choice. It is a biological imperat ive. And just as 
evolution favored human beings who were able to stand upright, it favored human beings who 
felt love. It favored them because love has great survival value.” (Acker man, 151).   But what is 
this love, why are we driven to achieve it, and why are we so despondent when it’s miss ing from 
our lives?  In order to understand and answer these questions, it is imperative to tra vel through 
history, and to discuss how love was understood in the past.   
 In ancient Greece, Athens was considered the “birthplace of western philosophy .”  The 
family was not as we know it to be today.  “…the family was not one household in Athens; it 
was the city itself, whose affairs all men knew and played a role in…Once le gitimate heirs were 
born to a man, things loosened up slightly for the wives, who could then divorce to get out of a 
particularly nasty marriage.” (Ackerman, 23).  While there were, unquestionabl y, extramarital 
affairs, they were more well-known and accepted in that society.  There is  a similarity in one 
aspect, however. “It’s not that Athenian women didn’t sometimes have premarita l or extramarital 
affairs, but those who did were thought shocking and immoral.” (Ackerman, 23).  This idea  is 
still true in today’s society, men’s affairs are almost accepted, and a t the very least, they aren’t 
seen to be as much of a scandal of that of women’s affairs.   
 With the knowledge of extramarital affairs and divorce, one may wonder if the anc ient 
Greeks believed in love.  In fact, the belief that society holds today, that there i s one person out 
there for everyone, a “soul mate”, actually originated with Plato.  Plato (429 –347 B.C.E.) 23 
LOVE 
discussed the idea of the soul being separate from the body. “We must recogni ze that the soul is 
a different sort of object from the body — so much so that it does not depend on the existence of 
the body for its functioning, and can in fact grasp the nature of the forms far more e asily when it 
is not encumbered by its attachment to anything corporea.” (Kraut, 2009).  In additi on, “the 
preconceived image of the person we are meant to love comes from Plato, who said t hat there are 
perfect universal forms, and humans are constantly searching for facsimil es of those forms.” 
(Ackerman, 126).  Plato’s idea, that there is someone out there for everyone, is what kee ps 
everyone searching for adoration and love.  We, as a society, are taught, from the very  
beginning, that love is real, our soul mates are out there, and, ultimately, we will fi nd the one 
who makes us complete and whole.   
 Perhaps couples stay together because of Plato’s idea of “soul mates”. When coupl es get 
married, those who are religious feel that they have found their soul mates, and t hey make a 
solemn promise to God to make the marriage work and flourish.  In getting a divorce, the couple 
not only has to admit defeat to themselves, but also break a promise to God.  They have to admi t 
that the person they married may not be their “soul mate”, and that can be terrifyi ng, because 
they need to go back out into the world of dating.  Some of them may have the faith that they  
will find their love, others may meet and fall in love with someone else who may not be r ight for 
them.  All of this work is done in search of a “soul mate”. 
 A more modern philosopher, Michael Boylan, discusses his idea of love in his book The 
Good, The True and The Beautiful . He states that love is an action, and the concept leads us to 
change and grow as human beings.  “Love is a powerful motivator for being good. The  affective 
part of the good will is no poor sister to the rational. It can be an effective gui de to good action.”  24 
LOVE 
(27).  One can conclude, then, that the essence of love is not only to find your soul mate, but it 
also allows one to be “good”.   
 Finally, one must philosophically compare love and sex, since these two ideas have  a 
biological and psychological basis.  Another modern philosopher, Robert Rowland Smith, does 
just that in his book Breakfast with Socrates .  He concludes that “According to biblical tradition 
love can, in turn, be subdivided into friendship (philia) and spiritual or emotional love (agape) , 
which complicates the relationship with sex, or eros, a bit further.” (198). This the ory, a 
complication of love and sex, is one that has been discussed for generations.  Harlan E llison once 
concluded that “Love ain't nothing but sex misspelled.” While this quote is often la ughed off, 
there is some truth to the saying.  Love and sex are absolutely entangled; howe ver it is possible 
to have one without the other.  But that’s a story, and a lesson, for another day. 
 In an interview with William Krieger, the philosophical aspect of love wa s discussed.  
Dr. Krieger stated that “psychology started from philosophy”, and that both of the se disciplines 
are entangled.  Considering the research that was done based on Plato and Socrates’  work, it’s 
not difficult to see how these two disciplines play off and complement one another.  When asked 
what he thought was the reason couples are able to stay together, Dr. Krieger st ated it was due to 
“a person’s ability to change.”  When asked to clarify on that idea, Dr. Kriege r stated “people 
change radically over time; the couples have to be able to change as well.”  This  idea is similar to 
Ms. Kinsey’s, that in order for a marriage to survive, a person has to be able to chang e, to be 
flexible and resilient.   
 Dr. Krieger also agreed with Ms. Kinsey’s idea that there is less of a stigm a surrounding 
divorce in today’s society.  He stated that “years ago, women had no opportunities…eve n less if 
you had kids.”  In addition to the stigma surrounding divorce being lessened, Dr. Krieger  also 25 
LOVE 
stated that there is less stigma surrounding the concept of seeking therapy.  Couples are now able 
to feel more free to visit a therapist in order to work through their difficulties , and in this way, 
they are able to potentially save some marriages that would have ended in di vorce. 
 Dr. Krieger also concurs with Dr. Zawia and Ms. Kinsey, insofar as he believe s that love 
and successful marriages are due to a combination of biology, psychology and philosophical  
aspects.  He stated that “neurochemistry is definitely important, but it’s not al l of it.”  Dr. Krieger 
states that he absolutely believes in love and marriage, and that it is important to w ork together 
and change with the relationship in order to make it successful.  He concludes that “L ife is too 
short to be terribly miserable.”  
  
Biology, Psychology, Philosophy: Who wins? 
  After researching all three areas of love, it is difficult to say which o f them is the most 
important when it comes to love, marriage, and success in a relationship.  Biologic al factors, 
such as the release of the hormones and neurotransmitters, are absolutely import ant in falling in 
love, and staying in love.  Evolutionarily speaking, pheromones are also extremely impor tant in 
finding the best mate, especially if one wants to have children and give them the best  chance of 
survival, thanks to the MHC.   
 Psychological aspects, such as Freud’s ideas of the way one picks their mate  based on 
their relationship with their parents, and also their regression into irrational be havior when in 
love, is also equally important.  The fact that Maslow has both the ideas of “safety  and security” 
and “love and belonging” in his hierarchy is important, because it allows one to recog nize that 
love isn’t just a random concept, it is necessary for good mental health.  Skinner’s ex planation of 26 
LOVE 
the positive reinforcement involved in operant conditioning allows us insight in how psycholog y 
explains and reinforces love.   
 Finally, Plato’s discussion of the idea of a “soul mate” is crucial to today’ s idea of love.  
We spend a considerable amount of time searching for our soul mates; some of us spend our 
entire lives, just to feel the type of love that Plato described. Michael Boy lan’s idea that love is a 
means towards doing ‘good’ can be seen everywhere.  A person may donate an organ or bone  
marrow to a loved one.  We help our loved ones work through issues that would be ignored if 
they were a stranger.  The idea that love is an impetus for good embodies the esse nce of the 
human spirit.  Finally, Robert Rowland Smith’s idea of love and sex being intertwined brin gs 
new meaning to sex, turning it from a biological drive to something beautiful share d by humans, 
in order to feel closer to one another.  
 In conclusion, more research needs to be done in order to discover what love truly is.  
While the previous research is extremely beneficial in helping to define love, c ase studies of 
couples who have been married for a substantial amount of time (greater than twent y-five years) 
would be helpful in order to come to a more definite conclusion.  While no final definition of 
love has been concluded, a quote from Pascal comes the closest to gleaning a clue:  "T he heart 
has reasons that reason cannot know." 
 
 
 
 
 
 27 
LOVE 
References 
 
Ackerman, D. (1994). A natural history of love . New York, NY: Random House, Inc. 
 
Boylan, M. (2008). The good, the true, and the beautiful.  New York, NY: Continuum 
 International Publishing Group. 
 
Drabble, M., Stringer, J."Freud, Sigmund." The Concise Oxford Companion to English 
 Literature . 2003. Retrieved November 29, 2010 from Encyclopedia.com: 
 http://www.encyclopedia.com/doc/1O54-FreudSigmund.html  
 
Kraut, Richard, "Plato", The Stanford Encyclopedia of Philosophy (Fall 2009 Edition) , Edward 
 N. Zalta (ed.), http://plato.stanford.edu/archives/fall2009/entries/plato/. 
 
Pincott, J. (2008). Do gentlemen really prefer blondes?: Bodies, behavior and brains- The 
 science behind sex, love & attraction.  New York, NY: Random House, Inc.  
 
Selhub, E. (2009). The love response . New York, NY: Random House, Inc. 
 
 Shakespeare, W.(1964). The tragedy of Romeo and Juliet.  Bryant, J.A. (Ed.).  New York, NY. 
 Signet. 
 28 
LOVE 
Sherwood, L. (2006). Fundamentals of physiology: A human perspective.  Belmont, CA: 
 Thomson Brooks/Cole 
 
"Sigmund Freud." The Columbia Encyclopedia, Sixth Edition . 2008. Retrieved November 29, 
 2010 from Encyclopedia.com: http://www.encyclopedia.com/doc/1E1-Freud-Si.html  
 
Smith, R.R. (2009). Breakfast with Socrates . New York, NY: Simon & Schuster, Inc. 
 
Varcarolis, E.M. & Halter, M.J. (2010). Foundations of psychiatric mental health nursing: A 
 clinical approach.  St. Louis: Elsevier, Inc.  
 
  
 
 
 
 
 
 
 
 '''
# Initialize NLTK components
stopwords_set = set(stopwords.words("english"))
stemmer = SnowballStemmer("english", ignore_stopwords=True)

# Function to summarize text
def summarize(text):
    # Preprocess text
    processed_text = re.sub("[^a-zA-Z' ]+", " ", text)
    words = word_tokenize(processed_text)
    
    # Build word frequency table
    freq_table = {}
    for word in words:
        word = word.lower()
        if word not in stopwords_set:
            stemmed_word = stemmer.stem(word)
            freq_table[stemmed_word] = freq_table.get(stemmed_word, 0) + 1

    # Normalize sentences
    sentences = sent_tokenize(text)
    sentence_values = {}
    for sentence in sentences:
        for word_value in freq_table:
            if word_value in sentence.lower():
                sentence_values[sentence] = sentence_values.get(sentence, 0) + freq_table[word_value]

    # Calculate average sentence value
    average_value = sum(sentence_values.values()) / len(sentence_values)

    # Create summary
    summary = " ".join(sentence for sentence in sentences if sentence_values.get(sentence, 0) > 1.5 * average_value)
    return summary
    # processed_text = re.sub("[^a-zA-Z' ]+", " ", text)
    # words = word_tokenize(processed_text)
    # stopWords = {"needn't", 'be', 'his', 'all', 'under', 'which', "haven't", 'won', 'you', "couldn't", 'then', 'between', 'having', 'll', 'yourselves', 'or', 'down', 'don', 'theirs', 's', 'what', 'because', 'am', 'their', 'against', "it's", 'my', 'why', 'had', 'couldn', 'your', 'was', 'here', 'with', 'out', 'should', 'about', 'them', 'too', 'been', "you've", 'most', 'ain', "you'd", 'm', 'before', "hadn't", 'needn', 'other', 'doesn', 'very', 'are', "mustn't", 'that', 'ours', 'didn', 'mightn', "didn't", 'i', 'but', 'is', 'in', 'to', 'such', 'so', 'no', "aren't", 'into', 'when', 'will', 'wouldn', 'if', 'own', "you'll", 'who', 'aren', 'have', 'we', 'by', 'where', 'during', 'its', 'now', 'than', "weren't", 'she', 'and', 'below', 'being', 'ourselves', 'haven', 'can', 'both', 'they', 'he', 'doing', 'only', 'herself', 'itself', 'each', 'hadn', 'weren', 'isn', "mightn't", 'more', 'shouldn', 'how', 'nor', "you're", 'were', 'from', "should've", 'of', 'wasn', 'a', 'her', 'until', 'him', 'hers', 'again', 'o', "isn't", 'those', 'yourself', "hasn't", "wouldn't", 'hasn', 't', 'any', 'shan', 'this', "she's", 'just', 'yours', 'the', 'd', 'few', 've', 'an', 'further', 'myself', "that'll", 'for', "shouldn't", 'above', 'whom', 'not', 'same', 'does', 'y', 'it', 're', 'through', 'while', 'after', "doesn't", 'mustn', "won't", 'some', 'once', 'himself', 'at', 'as', 'our', 'over', "don't", "shan't", 'has', 'do', 'ma', 'on', 'these', 'did', 'there', 'off', 'me', 'up', 'themselves', "wasn't"}

    # stemmer = SnowballStemmer("english", ignore_stopwords=True)
    # freqTable = dict()
    # for word in words:
    #     word = word.lower()
    #     if word in stopWords:
    #         continue
    #     elif stemmer.stem(word) in freqTable:
    #         freqTable[stemmer.stem(word)] += 1
    #     else:
    #         freqTable[stemmer.stem(word)] = 1

    # # Normalize every sentence in the text
    # sentences = sent_tokenize(text)
    # stemmedSentences = []
    # sentenceValue = dict()
    # for sentence in sentences:
    #     stemmedSentence = []
    #     for word in sentence.lower().split():
    #         stemmedSentence.append(stemmer.stem(word))
    #     stemmedSentences.append(stemmedSentence)

    # # Calculate value of every normalized sentence based on word frequency table
    # # [:12] helps to save space
    # for num in range(len(stemmedSentences)):
    #     for wordValue in freqTable:
    #         if wordValue in stemmedSentences[num]:
    #             if sentences[num][:12] in sentenceValue:
    #                 sentenceValue[sentences[num][:12]] += freqTable.get(wordValue)
    #             else:
    #                 sentenceValue[sentences[num][:12]] = freqTable.get(wordValue)

    # # Determine average value of a sentence in the text
    # sumValues = 0
    # for sentence in sentenceValue:
    #     sumValues += sentenceValue.get(sentence)

    # average = int(sumValues / len(sentenceValue))

    # # Create summary of text using sentences that exceed the average value by some factor
    # # This factor can be adjusted to reduce/expand the length of the summary
    # summary = ""
    # for sentence in sentences:
    #         if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (3.0 * average):
    #             summary += " " + " ".join(sentence.split())

    # # Process the text in summary and write it to a new file
    # summary = re.sub("’", "'", summary)
    # summary = re.sub("[^a-zA-Z0-9'\"():;,.!?— ]+", " ", summary)
    # return summary

# Process lines from stdin
for line in a:
    line = line.strip()
    file_name, text = line.split("\t", 1)
    summary = summarize(text)
    print(f"{file_name}\t{summary}")