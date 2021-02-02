"""Constants used for in tests"""

MOCK_TWEETS = [{'created_at': '2021-02-01T09:06:14.000Z', 'id': '1356166962372608000',
                'text': 'Everyone needs to watch this.\n#COVID19 #COVID \nINFLUENCER-19 https://t.co/fF6IEpWK2X via '
                        '@YouTube @dangelno'},
               {'created_at': '2021-02-01T09:06:08.000Z', 'id': '1356166934589530112',
                'text': 'RT @UWPharmacy: How mRNA #COVID vaccines work, from @kgrindrod with help from @NoahIvers, '
                        '@19ToZero &amp; @RosemaryKilleen\nMore resources here:…'},
               {'created_at': '2021-02-01T09:06:05.000Z', 'id': '1356166924053270530',
                'text': "RT @TheDailyPioneer: Superb #Budget. It'll not only accelerate us in pre-#COVID period "
                        "recovery stage but also provide a direction for 3-4…"},
               {'created_at': '2021-02-01T09:06:05.000Z', 'id': '1356166923717922816',
                'text': '@BBCBreaking RT #Ivermectin KILLS BAD #COVID-19 IN 2-6 DAYS: my 90-yro Aunt, on edge of '
                        'intubation, ICU, on heavy oxygen, got rid of it in 5 days; feeling better after 1. '
                        'Webinar https://t.co/BHrTWF4B8Y\n&amp; protocol https://t.co/V6HdGvSJEA $2/day. '
                        'Get it approved, please!'},
               {'created_at': '2021-02-01T09:06:03.000Z', 'id': '1356166914389671938',
                'text': 'EU meets drug giants for rapid development of vaccines against new COVID-19 variants \n '
                        '#COVID-19NewStrain #COVID-19Vaccine #ModernaCOVID-19Vaccine #Pfizer \n '
                        'https://t.co/Cdbb1YZtdB'},
               {'created_at': '2021-02-01T09:06:01.000Z', 'id': '1356166908144451585',
                'text': 'Switzerland calls referendum on stopping #Covid lockdowns - Business Insider '
                        'https://t.co/osjGT6KcnL'},
               {'created_at': '2021-02-01T09:06:01.000Z', 'id': '1356166906194104320',
                'text': 'RT @RACHELb75: A thread on our #Covid Experience-my husband and I tested positive for it on '
                        '13th January, and quickly became symptomatic ov…'},
               {'created_at': '2021-02-01T09:05:58.000Z', 'id': '1356166895658020866',
                'text': "'We're in a storm': medical students on the #Covid frontline. https://t.co/acrrf2cXEk"},
               {'created_at': '2021-02-01T09:05:55.000Z', 'id': '1356166879614668801',
                'text': 'RT @Torontonicity: It looks like most people will be spending #ValentinesDay at home in 2021. '
                        'Here are a few #ideas for your stay-at-home V…'},
               {'created_at': '2021-02-01T09:05:50.000Z', 'id': '1356166860371156994',
                'text': "@Karma6X @Swamy39 @Rumm17913821 @vishalnautamlal @nviswam @colkt @Treasure1725 @Geethabhati "
                        "@apar_chu @GurudathShettyK @ragusmg2 @RupamDu22916188 @Lutyensmafia @MrRao_RB "
                        "@chitrapadhi @Shawshanko @naveen_42_ @VarshaThacker @NATRAJSHETTY @mm_0774 @8Y8ZQ "
                        "@brahmavidvariya @ravi_enigma @SwamyBhakt @Bhaskarg77G @vijay2474 @REIyer4 @jagdishshetty"
                        " @ArvindChaturved @MD_Nalapat Superb #Budget. It'll not only accelerate us in pre-#COVID "
                        "period recovery stage but also provide a direction for 3-4 yrs. Govt focused on infrastructure"
                        " &amp; asset monetization this time...Shows Govt's thinking that it's essential to involve pvt"
                        " sector in long run: #NITIAayog CEO https://t.co/wWk9QYvZM9"},
               {'created_at': '2021-02-01T09:05:41.000Z', 'id': '1356166821498540032',
                'text': 'BREAKING: BioNTech/Pfizer pledge up to 75 million extra vaccine doses to EU #COVID '
                        'https://t.co/rfgP3YmJGn'},
               {'created_at': '2021-02-01T09:05:33.000Z', 'id': '1356166786950057984',
                'text': "Why aren't more people asking? #90day madness no cover till 2nd dose = more deaths + longer "
                        "#lockdownuk Share on #Twitter #blair is #war criminal #covid https://t.co/rPnKsE3rNc"},
               {'created_at': '2021-02-01T09:05:30.000Z', 'id': '1356166777659658247',
                'text': '3/3 \n🤤 Dick has a continuous dry cough and feels unwell. He’s hoping it’s not #Covid but '
                        'has gone out anyway. 𝐃𝐨𝐧’𝐭 𝐚𝐜𝐭 𝐥𝐢𝐤𝐞 𝐚 𝐃𝐢𝐜𝐤. https://t.co/vy0UyiGPcA'},
               {'created_at': '2021-02-01T09:05:22.000Z', 'id': '1356166744201715719',
                'text': 'Great shift on Guildford Ward (our covid ward) @RoyalSurrey Fabulous to support the amazing '
                        'staff that have all been working so hard. And I got to wear the fabulous rainbow 🌈 '
                        'scrubs 💗 #COVID #StayAtHome https://t.co/oY9CZRU5lW'},
               {'created_at': '2021-02-01T09:05:21.000Z', 'id': '1356166738824454151',
                'text': 'Great to see amazing leadership from the ADA (WA Branch) guiding dental practices on how to '
                        'comply with level 3 restrictions #dentistry #perth #covid'},
               {'created_at': '2021-02-01T09:05:05.000Z', 'id': '1356166671698976768',
                'text': 'RT @SabinaLeonelli: What has the #COVID pandemic taught us about data-intensive research '
                        '&amp; its future? What is the role of values, politics…'},
               {'created_at': '2021-02-01T09:05:04.000Z', 'id': '1356166668683251714',
                'text': 'RT @LkoSmartCity: #IndiaFightsCorona\n\nLet’s join our hands to strengthen India’s fight '
                        'against #COVID-19 by taking the pledge to take all t…'},
               {'created_at': '2021-02-01T09:05:04.000Z', 'id': '1356166666590146563',
                'text': "I unfortunately got covid and it's the  worst thing that I've ever gone through . "
                        "Currently at UMC trying to see if I'm dying or not . Apparently I'm not according to medical "
                        "professionals. \n#COVID #WearYourMask #6feetapart"},
               {'created_at': '2021-02-01T09:05:02.000Z', 'id': '1356166659149619201',
                'text': 'RT @FlorenceSSG: @Keir_Starmer “I’ve got children at home. I’m not ready. I can’t die!” \nShe '
                        'is 35 years old. She FaceTimes her children &amp;…'},
               {'created_at': '2021-02-01T09:04:58.000Z', 'id': '1356166642003271680',
                'text': '🙁 Harriet’s partner is unwell with #Covid, so she’s following guidance and is self-isolating.'
                        ' They’ve had help with shopping from a kind neighbour. \n𝐀𝐜𝐭 𝐦𝐨𝐫𝐞 𝐥𝐢𝐤𝐞 𝐚 𝐇𝐚𝐫𝐫𝐢𝐞𝐭.'},
               {'created_at': '2021-02-01T09:04:43.000Z', 'id': '1356166577826234371',
                'text': "Sad really. I'd put everything I own on the line the true reason he was admitted is pneumonia "
                        "related. Now they're stating from the very start people are getting admitted for #covid. "
                        "Quite clever really if he and others do sadly pass away. https://t.co/CF6ceY7VOw"},
               {'created_at': '2021-02-01T09:04:41.000Z', 'id': '1356166572163870723',
                'text': '@DavidHenigUK @NickStevenson63 You flip a coin enough times, you get three heads in a row.'
                        '\n\nJohnson ‘s #covid ’strategy’ has been one huge risky bet after another.\n\nI am '
                        'pleased Brits are getting vaccinated.'},
               {'created_at': '2021-02-01T09:04:40.000Z', 'id': '1356166564651753472',
                'text': 'RT @Sanju_Verma_: Apart from focus on health, education&amp;Infra,do note the eye for detail'
                        '\n\nRs1000Cr for Assam #Tea workers\n\nRs 1 lakh Cr for…'},
               {'created_at': '2021-02-01T09:04:39.000Z', 'id': '1356166563129393155',
                'text': 'RT @scrowder: Want to invest? Biden-backed Wall St. will box you out. Want to speak? '
                        'Biden-backed Big Tech will ban you. Want to work? Bide…'},
               {'created_at': '2021-02-01T09:04:34.000Z', 'id': '1356166540517732352',
                'text': "Superb #Budget. It'll not only accelerate us in pre-#COVID period recovery stage but also "
                        "provide a direction for 3-4 yrs. Govt focussed on infrastructure &amp; asset "
                        "monetisation this time...Shows Govt's thinking that it's essential to involve pvt sector "
                        "in long run: #NITIAayog CEO https://t.co/5XhLtzJt4U"},
               {'created_at': '2021-02-01T09:04:31.000Z', 'id': '1356166530048921602',
                'text': 'RT @EmilyLGould: #Covid vaccine done. Must say #shrewsbury hub was fantastic. All so friendly'
                        ' and put me right at ease. Well done @NHSEngla…'},
               {'created_at': '2021-02-01T09:04:31.000Z', 'id': '1356166528815804417',
                'text': 'RT @VABVOX: I am having a very tough time with heart and lung problems from the virus. 40% '
                        'or more of people who get #COVID will have long-…'},
               {'created_at': '2021-02-01T09:04:30.000Z', 'id': '1356166525623939074',
                'text': 'RT @alexstubb: Very impressed with Finnish public sector #Covid testing. Took my 16th test '
                        'today. Booked a time online with @HUS_uutisoi bo…'},
               {'created_at': '2021-02-01T09:04:13.000Z', 'id': '1356166453398032384',
                'text': 'RT @WesElyMD: Death💀of a team member from #COVID19 is especially brutal. Nashville TN USA '
                        '#nurses #nursepractitioner #physicianassistant #r…'},
               {'created_at': '2021-02-01T09:04:09.000Z', 'id': '1356166435693854723',
                'text': 'RT @michaeldickson: 33% of the Israeli population have now had their first #Covid vaccination.'
                        ' Over 18% have had their second dose.'},
               {'created_at': '2021-02-01T09:04:06.000Z', 'id': '1356166425023373314',
                'text': 'The frustrating and liberating ways travel is returning in 2021\n#Uncategorized #Air #Travel '
                        '#Coronavirus #Covid #Testing #Covid-19 #Edited #By #Jackie #Bischof #Hotels '
                        '#Pandemic #Tourism #Travel #Vaccine #Certificate #Borders #Lifestyle #Travel '
                        '#In #2021\nhttps://t.co/fVxXe1tZFL'},
               {'created_at': '2021-02-01T09:04:06.000Z', 'id': '1356166423706558467',
                'text': '@LBC @NickFerrariLBC Yes this is only one #thing I #agree with #TonyBlair I am #happy to give '
                        'my #covid #vaccine to #Teachers'},
               {'created_at': '2021-02-01T09:04:05.000Z', 'id': '1356166418962767873',
                'text': 'RT @aier: "We present 31 high-quality sources of evidence [which] show that #COVID #lockdowns '
                        'have been a failure."\n\nDr. Paul E. Alexander,…'},
               {'created_at': '2021-02-01T09:04:05.000Z', 'id': '1356166417838706692',
                'text': 'RT @PathwayConsGrp: So this week we hear about the litigious guest, issuing repeatedly to date'
                        ' across multiple #hospitality locations...not…'},
               {'created_at': '2021-02-01T09:03:53.000Z', 'id': '1356166368635342851',
                'text': 'RT @VABVOX: I am having a very tough time with heart and lung problems from the virus. 40% or'
                        ' more of people who get #COVID will have long-…'},
               {'created_at': '2021-02-01T09:03:52.000Z', 'id': '1356166364743032833',
                'text': 'RT @PathwayConsGrp: The events surrounding #BLM shone a blazing light on '
                        '#diversityandinclusion'
                        ' and #protectedcharacteristics under #equali…'},
               {'created_at': '2021-02-01T09:03:50.000Z', 'id': '1356166357008609286',
                'text': '#Auspol Is it just me or is there something morally wrong with any Australian government, if '
                        'you believe the media,  deciding whether or not to call an early election, '
                        'based on how successful they were in vaccinating the people for #COVID ?\n\nIn other words - '
                        'they did their job!!!'},
               {'created_at': '2021-02-01T09:03:49.000Z', 'id': '1356166352889851912',
                'text': "RT @sjriches: Our new article 'Brief videoconference-based Dialectical "
                        "Behaviour Therapy skills"
                        " training for Covid-19-related stress in acu…"},
               {'created_at': '2021-02-01T09:03:49.000Z', 'id': '1356166352134840320',
                'text': 'Fiscal deficit at 9.8% of GDP, quite courageous step. Much needed to revive t'
                        'he #covid burdened economy #Budget2021 https://t.co/pSRs896Jdb'},
               {'created_at': '2021-02-01T09:03:49.000Z', 'id': '1356166351417716738',
                'text': '#BreakingNews\n#COVID-19 Defaulters Risk Jail Term as Buhari Signs COVID-19 Health Protection '
                        'Regulations 2021 Policy\n\nPresident Muhammadu Buhari, last Wednesday, signed Coronavirus '
                        '(COVID-19) Health Protection Regulations 2021 policy. \n\n.@NCDCgov'},
               {'created_at': '2021-02-01T09:03:43.000Z', 'id': '1356166329380839426',
                'text': 'RT @midletonimages: If you look closely when walking in East Ferry there are lots of Snowdrops'
                        ' appearing! \n@pure_cork @corkbeo \n@PhotosCork…'},
               {'created_at': '2021-02-01T09:03:32.000Z', 'id': '1356166280739512321',
                'text': 'RT @i24NEWS_EN: #Israel: 5,140 new #covid cases found in last 24 hours, positivity rate at '
                        '9.7%\nhttps://t.co/8AGTRBjFdh'},
               {'created_at': '2021-02-01T09:03:31.000Z', 'id': '1356166278621196293',
                'text': 'RT @KunalSarangi: India’s preparedness for a ‘V’ shaped recovery post #COVID is evident right '
                        'from the #UnionBudget2021 app, @nsitharaman J…'},
               {'created_at': '2021-02-01T09:03:30.000Z', 'id': '1356166274120749062',
                'text': 'Vaccine for Corona!!!\nHow vaccine are developed? To know more check out this video\n\n'
                        'https://t.co/CSzftnySRZ\n\n#CoronaVaccine #Covaxin #Covishield #COVID19 #CovidVaccine '
                        '#COVIDー19 #coronavirus #COVID #India #diplomacy'},
               {'created_at': '2021-02-01T09:03:21.000Z', 'id': '1356166236334399488',
                'text': "#UK jigsaw #puzzle sales hit £100m as 'people find a balance in their lives' "
                        "https://t.co/wO7Sn2z8HW #covid #lockdown"},
               {'created_at': '2021-02-01T09:03:21.000Z', 'id': '1356166234753134593',
                'text': 'RT @francewitch: MY COUSIN IS STILL REALLY ILL in hospital with this damned disease. He lost '
                        'his mother, father and sister to it within the…'},
               {'created_at': '2021-02-01T09:03:19.000Z', 'id': '1356166228608479232',
                'text': 'RT @francewitch: MY COUSIN IS STILL REALLY ILL in hospital with this damned disease. He lost '
                        'his mother, father and sister to it within the…'},
               {'created_at': '2021-02-01T09:03:15.000Z', 'id': '1356166210086440968',
                'text': 'RT @afbranco: A.F. Branco Cartoon - Bad to worse https://t.co/W1Jgvx6Yuc via @alphanewsmn '
                        '#COVID19 #COVID #SmallBusinesses #Minnesota https…'},
               {'created_at': '2021-02-01T09:03:09.000Z', 'id': '1356166185969209345',
                'text': 'RT @IntEpilepsyDay: If you/your organisation are taking place in the #50MillionSteps campaign '
                        'to raise #epilepsy awareness, please be sure…'},
               {'created_at': '2021-02-01T09:03:08.000Z', 'id': '1356166182253031427',
                'text': 'Wear your nose masks. And assume that the person next to you has COVID '
                        '\n\n#COVID #CovidVaccine'
                        ' #nosemask #February2021 #mondaythoughts'},
               {'newest_id': '1356167637114396676', 'oldest_id': '1356166182253031427', 'result_count': 100,
                'next_token': 'b26v89c19zqg8o3fosktzh8bhwn9j9nv0vldqte96etml'},
               {'created_at': '2021-02-01T09:03:02.000Z', 'id': '1356166156768342024',
                'text': 'RT @Sanju_Verma_: Apart from focus on health, education&amp;Infra,do note the eye for detail'
                        '\n\nRs1000Cr for Assam #Tea workers\n\nRs 1 lakh Cr for…'},
               {'created_at': '2021-02-01T09:03:02.000Z', 'id': '1356166154746736644',
                'text': 'Our main aim is to improve and streamline your business processes enabling you to thrive '
                        'in an ever changing business environment. \n#servicemanagement  #coronavirus #covid #tech\n\n'
                        'https://t.co/aUVqDv9VQE https://t.co/nk9WGv4GZV'},
               {'created_at': '2021-02-01T09:02:56.000Z', 'id': '1356166129023152131',
                'text': "This is such fabulous news! I can't wait for the day when I can hug my dad, sit with him, "
                        "look at photos. Last time I did that was 30 Dec 2019. Luckily he's survived #Covid "
                        "but #dementia ravages the mind, day by day #carehome #vaccine #coronavirus "
                        "\nhttps://t.co/xw8fxV5kBj"},
               {'created_at': '2021-02-01T09:02:53.000Z', 'id': '1356166116771569664',
                'text': '#CovidVaccine #covid. When will we find out that one dose is not enough. @piersmorgan '
                        '@afneil @KateEMcCann GENUINE QEUSTION.'},
               {'created_at': '2021-02-01T09:02:51.000Z', 'id': '1356166108093550592',
                'text': '@rec777777 @mrconnorgotto @BBCBreakfast @GMB Footnote: #Vaccine doesn’t stop you '
                        'catching #covid it is a gene therapy that can limit it’s severity.'},
               {'created_at': '2021-02-01T09:02:38.000Z', 'id': '1356166055987736576',
                'text': 'RT @aier: "We present 31 high-quality sources of evidence [which] show that #COVID '
                        '#lockdowns have been a failure."\n\nDr. Paul E. Alexander,…'},
               {'created_at': '2021-02-01T09:02:07.000Z', 'id': '1356165926165467136',
                'text': 'RT @Sanju_Verma_: Apart from focus on health, education&amp;Infra,do note the eye '
                        'for detail\n\nRs1000Cr for Assam #Tea workers\n\nRs 1 lakh Cr for…'},
               {'created_at': '2021-02-01T09:02:03.000Z', 'id': '1356165908658532353',
                'text': 'RT @FarmFutures: #COVID-19 disrupts #food consumption patterns\n#CoBank report '
                        'predicts #foodservice sales will return to #pre-pandemic leve…'},
               {'created_at': '2021-02-01T09:02:03.000Z', 'id': '1356165906565640192',
                'text': '@NationalCareAsc @careuk you need confirmation from @Helen_Whatley if @GOVUK '
                        'plans to force care staff to get the #covid vaccine. When asked by @JustinOnWeb '
                        'this morning if staff would be \'encouraged\' she twice used the phrase "At the moment". '
                        'Worrying implications right there!'},
               {'created_at': '2021-02-01T09:02:02.000Z', 'id': '1356165905458327553',
                'text': 'RT @scrowder: Want to invest? Biden-backed Wall St. will box you out. Want to '
                        'speak? Biden-backed Big Tech will ban you. Want to work? Bide…'},
               {'created_at': '2021-02-01T09:01:44.000Z', 'id': '1356165826668331009',
                'text': 'RT @Saj_PakPassion: Moeen Ali "I\'ll take the vaccine &amp; urge others to. '
                        'It\'s like any vaccine - there\'s conspiracy theories but it\'s just me…'},
               {'created_at': '2021-02-01T09:01:43.000Z', 'id': '1356165823220625412',
                'text': 'RT @MaritimeProgres: Keep your crew, staff &amp; passengers safe with #Covid '
                        '#safetysigns and posters . https://t.co/tLtV6Nv5vo https://t.co/to…'},
               {'created_at': '2021-02-01T09:01:42.000Z', 'id': '1356165818149695488',
                'text': 'MLB Opening Day is always one of my favorite days to look forward to and even with '
                        '#Covid I still was glad to be a part of it https://t.co/TB1o5Pu4UR #baseball '
                        '#sports #sportsphotographer'},
               {'created_at': '2021-02-01T09:01:38.000Z', 'id': '1356165802429452288',
                'text': 'Wouldn’t matter if he had if had it in relation to #catching #covid #virus the '
                        '‘vaccine’ doesn’t stop you catching it... https://t.co/ACZ1NqYNdi'},
               {'created_at': '2021-02-01T09:01:36.000Z', 'id': '1356165795706003460',
                'text': 'Apart from focus on health, education&amp;Infra,do note the eye for detail\n\nRs1000Cr for '
                        'Assam #Tea workers\n\nRs 1 lakh Cr for UTs of Jammu, #Kashmir&amp; #Ladakh,to be funded '
                        'entirely by @narendramodi govt\n\nMulti #SeaweedPark in TN👍\n\nRs35400 for #Covid vaccine '
                        '&amp;3758Cr for #DigitalCensus'},
               {'created_at': '2021-02-01T09:01:20.000Z', 'id': '1356165729217880152',
                'text': 'Peopleperhour Partners With Indeez to Provide Industry-First #COVID #Insurance for '
                        '#Freelancers https://t.co/YRMMRnWIeC https://t.co/eUy8Bvz7oQ'},
               {'created_at': '2021-02-01T09:01:14.000Z', 'id': '1356165702709862401',
                'text': 'Peopleperhour Partners With Indeez to Provide Industry-First #COVID #Insurance for '
                        '#Freelancers https://t.co/NFdE1ep7Nc https://t.co/qaBFDDllhQ'},
               {'created_at': '2021-02-01T09:01:14.000Z', 'id': '1356165701199925249',
                'text': "RT @BBCNuala: More candid stories from OS about the impact of #covid : The pandemic's "
                        "young widows and widowers -  thx to \u2066@readingswan\u2069 &amp;…"},
               {'created_at': '2021-02-01T09:01:13.000Z', 'id': '1356165699715129344',
                'text': '@theicfp will bring together scientists, advocates, leaders and '
                        'community members to discuss the intersections of #COVID-19, #UHC and #familyplanning.'
                        '\n\nJoin us at #ICFP2021 🙋\u200d♀️\n\nBecause there is no #UHC2030 without family '
                        'planning. 📣\n\n#NotWithoutFP #FPisEssential #HealthForAll https://t.co/WqbZP2voGF'},
               {'created_at': '2021-02-01T09:01:09.000Z', 'id': '1356165682971377666',
                'text': 'RT @DrLahariya: Summary: \nUnion #health budget increased by ~10% \n\nThe 137% '
                        'increase in wellness budget when we count as-hoc one time #COvI…'},
               {'created_at': '2021-02-01T09:01:06.000Z', 'id': '1356165669038002178',
                'text': '@LoftusOrla @Independent_ie @PracticeNurses @HSEImm @MichealMartinTD @chiefnurseIRE '
                        '@muirtheimhne @INMO_IRL @HSELive @paulreiddublin @GColleranMD @ICGPnews @gpbuddy need '
                        '4 #GP #PracticeNurses b under #HSE umbrella &amp; acknowledge crucial role they play, '
                        'moving forward with @slaintecare #primaryhealthcare &amp; #vaccine rollout #CovidVaccine '
                        '#COVID #Nursing @ICNurses'},
               {'created_at': '2021-02-01T09:01:05.000Z', 'id': '1356165665799868420',
                'text': 'For Antonio Banderas, beating Covid was his birthday gift #AntonioBanderas '
                        '#Covid https://t.co/ObuSiT62Se'},
               {'created_at': '2021-02-01T09:01:01.000Z', 'id': '1356165646959173634',
                'text': "RT @RealWineGuru: Tannins In #Wine Could Help To Inhibit #Covid-19. - "
                        "#Research from #Taiwan shows that #tannin's in wine can help fight #C…"},
               {'created_at': '2021-02-01T09:01:01.000Z', 'id': '1356165646178914304',
                'text': "RT @AaronKinKin1: Imagine if Australian's woke up tomorrow and realised "
                        "that every #Covid outbreak from #Rubyprincess to Victoria, to WA, w…"},
               {'created_at': '2021-02-01T09:00:57.000Z', 'id': '1356165630051770372',
                'text': 'RT @WesElyMD: Death💀of a team member from #COVID19 is especially brutal. '
                        'Nashville TN USA #nurses #nursepractitioner #physicianassistant #r…'},
               {'created_at': '2021-02-01T09:00:52.000Z', 'id': '1356165609789272068',
                'text': '#Covid safety products for the #office or #retail environment. We have a '
                        'range of #safetysolution products including #screens, and work space dividers/ '
                        'privacy screens. https://t.co/mEkHekv8gJ'},
               {'created_at': '2021-02-01T09:00:51.000Z', 'id': '1356165605578203137',
                'text': 'Covid-19 Gave Me Another Reason To Pursue My Dream More Than Ever! Learn More 👉🏻  '
                        'https://t.co/TtzTuPyKIN #gofundme #covid #dream #risemoney #vote'},
               {'created_at': '2021-02-01T09:00:51.000Z', 'id': '1356165604927922176',
                'text': 'ETHRWorld | British government working on COVID recovery plan for economy, says '
                        'source #CovidRecovery #Covid #FinanceMinistry #CabinetOffice #BritishGovernment '
                        '#International  https://t.co/W8KU7j22wI'},
               {'created_at': '2021-02-01T09:00:47.000Z', 'id': '1356165588398256129',
                'text': 'The #EUQuitters must be absolutely delighted with the prominence that ‘The English '
                        'Strain’ of #Covid is receiving around the World.\n\nTruly the ineptitude of '
                        '#JohnsonHasFailedTheNation’s response to the #pandemic has made ‘our’ #CoronaVirus '
                        '‘world beating’ https://t.co/IgwIfqbUTY'},
               {'created_at': '2021-02-01T09:00:41.000Z', 'id': '1356165562599145474',
                'text': 'An interesting BBC article showing the value of clean air in "massively reducing" '
                        'the risk of transmitting Covid. Clean air matters!\n\nhttps://t.co/mj2JEAoNAt #virus '
                        '#covıd #covid19safe #covid19safety #covid19awareness #healthcarehr #healthandsafetytraining '
                        '#economyrecovery https://t.co/KhW1doOfTD'},
               {'created_at': '2021-02-01T09:00:34.000Z', 'id': '1356165533067051008',
                'text': 'RT @Rich_Cooke1: Police,Prison Officers &amp; anyone else who is REQUIRED to mix &amp; '
                        'get close to other people should of been among the first to…'},
               {'created_at': '2021-02-01T09:00:33.000Z', 'id': '1356165531364188164',
                'text': '#Kenya to start #Covid-19 vaccinations this month on 1 million health workers - '
                        'https://t.co/WhPtypVeLD https://t.co/Pzrb5JsabA'},
               {'created_at': '2021-02-01T09:00:32.000Z', 'id': '1356165526016454656',
                'text': 'RT @Newzroom405: South Africa’s first #COVID-19 vaccines, that will land today won’t '
                        'be barcoded, which could make easier for criminals to…'},
               {'created_at': '2021-02-01T09:00:31.000Z', 'id': '1356165523411587077',
                'text': 'RT @EShearmur: Isolation. Once a popular concept... #glencoe #highlands #scotland #uk '
                        '#covid #isolation #landscapephotography https://t.co/…'},
               {'created_at': '2021-02-01T09:00:25.000Z', 'id': '1356165498044514312',
                'text': 'Tolisso fined, dropped by Bayern for breaking Covid-19 rules #Tolissofined #Bayern #Covid '
                        'https://t.co/K5QCoN7vRW'},
               {'created_at': '2021-02-01T09:00:22.000Z', 'id': '1356165483188412417',
                'text': 'RT @SabinaLeonelli: What has the #COVID pandemic taught us about data-intensive research '
                        '&amp; its future? What is the role of values, politics…'},
               {'created_at': '2021-02-01T09:00:21.000Z', 'id': '1356165480797642752',
                'text': 'RT @Saj_PakPassion: Moeen Ali "I\'ll take the vaccine &amp; urge others to. It\'s like '
                        'any vaccine - there\'s conspiracy theories but it\'s just me…'},
               {'created_at': '2021-02-01T09:00:19.000Z', 'id': '1356165470953627649',
                'text': '#IndiaFightsCorona\n\nLet’s join our hands to strengthen India’s fight against #COVID-19 by '
                        'taking the pledge to take all the necessary precautions &amp; follow all the guidelines to '
                        'protect ourselves and our loved ones. https://t.co/vDGyJQqLb3'},
               {'created_at': '2021-02-01T09:00:18.000Z', 'id': '1356165467572822020',
                'text': 'RT @MdIntek05336377: #GSTAmnestyJust like #COVID ー 19, for patients who require oxygen, '
                        'oxygen is needed to protect them, similarly busines…'},
               {'created_at': '2021-02-01T09:00:17.000Z', 'id': '1356165462711799808',
                'text': 'According to @thepmo, the new funding is designed to be an ‘initial allocation’ '
                        'to support the #COVID vaccination program, and more is expected to follow.  '
                        '#newsGP\nhttps://t.co/jdmy10vsYZ'},
               {'created_at': '2021-02-01T09:00:11.000Z', 'id': '1356165438137360386',
                'text': 'Hotel Equatorial #Penang bites the #Covid dust\nEnd of an era for a beloved '
                        'institution where many had fond memories of.\n\n#Hotels \nhttps://t.co/H17E3GSaBn '
                        'https://t.co/hChliux1iW'},
               {'created_at': '2021-02-01T09:00:10.000Z', 'id': '1356165433364279296',
                'text': 'New #restrictions have resulted in a 50% reduction in indoor #seatingcapacity, '
                        'which has a significant impact on your #revenue. 💰\n\nHere are some tips on making '
                        'your pub #COVID-proof, visit: https://t.co/CfOozE2RKZ'},
               {'created_at': '2021-02-01T09:00:05.000Z', 'id': '1356165414280163329',
                'text': 'RT @ACorps112: Some of our AP colleagues working with @NASCriticalCare as '
                        '#CriticalCareParamedic were tasked to a retrieval for a #Covid pa…'},
               {'created_at': '2021-02-01T09:00:04.000Z', 'id': '1356165407808368646',
                'text': "WION News - 'Sex and the City' revival will incorporate COVID-19 in the storyline\n "
                        "#COVID #WIONNews\n - https://t.co/0eJscH3OUZ\n    \n[https://t.co/Le5Szjt2uA]"},
               {'created_at': '2021-02-01T09:00:02.000Z', 'id': '1356165400669511681',
                'text': "Tune into 'The Health and Humor Show' with @MaureenSRN on @ukhealthradio - #Healthnews "
                        "including how to beat #COVID this year, your #wellnessIQ, and #heartattacks could be "
                        "predicted in advance with a simple #xray. 👉 🎧   "
                        "https://t.co/xhv77op7u5 https://t.co/Uf8Y6ovXMD"},
               {'created_at': '2021-02-01T09:00:02.000Z', 'id': '1356165399587352576',
                'text': '‘That hurricane is coming’: expert warns US to brace for virulent #Covid strain\n#coronavirus '
                        '#COVID19 https://t.co/M3w3ou6pY1'},
               {'created_at': '2021-02-01T09:00:01.000Z', 'id': '1356165395842002944',
                'text': 'Time to team up and tackle Long #COVID, says WHO expert https://t.co/0i3njbBo1r'},
               {'created_at': '2021-02-01T09:00:00.000Z', 'id': '1356165393551912961',
                'text': "Do you live in #northeastLondon? Are you aged 70+? Do you know anyone who is, &amp; "
                        "haven't received their #COVID-19 vaccination yet? No need to wait, book an appoinment "
                        "online now. Full details including link to online booking form here: https://t.co/w8ixFpXKls "
                        "https://t.co/xsmhj973Xa"}]

MOCK_TWEET = {
    'created_at': '2021-02-01T09:00:00.000Z',
    'id': '1356165393551912961',
    'text': """
            Tune into 'The Health and Humor Show' with @MaureenSRN on @ukhealthradio - #Healthnews including how to beat 
            #COVID this year, your #wellnessIQ, and #heartattacks could be predicted in advance with a simple #xray. 👉 🎧 
            $foobar https://t.co/xhv77op7u5 https://t.co/Uf8Y6ovXMD"
            """
}

MOCK_CLOUD_SUCCESS = {
    'first_tweet_timestamp': '01-02-2021 09:00:00 UTC',
    'last_tweet_timestamp': '01-02-2021 09:00:10 UTC',
    'topic': 'covid',
    'words': 100
}

MOCK_MAX_CLOUD = {
    'first_tweet_timestamp': '01-02-2021 09:00:00 UTC',
    'last_tweet_timestamp': '01-02-2021 09:06:14 UTC',
    'topic': 'covid',
    'words': 917
}

CSV_100_WORD_CLOUD = {
    'words': 'advance, aged, amp, an, and, anyone, ap, appoinment, are, as, be, beat, book, booking, brace, city, '
             'colleagues, coming, coronavirus, could, covid, criticalcareparamedic, details, do, expert, for, form, '
             'full, have, haven, health, healthnews, heartattacks, here, how, humor, hurricane, impact, in, including, '
             'incorporate, into, is, know, link, live, long, need, news, no, northeastlondon, now, of, on, online, our,'
             ' pa, predicted, received, restrictions, resulted, retrieval, revival, says, sex, show, simple, some, '
             'storyline, strain, tackle, tasked, team, that, the, their, this, time, to, tune, up, us, vaccination, '
             'virulent, visit, wait, warns, wellnessiq, were, who, will, wion, wionnews, with, working, xray, year, '
             'yet, you, your',
    'topic': 'covid', 'first_tweet_timestamp': '01-02-2021 09:00:00 UTC',
    'last_tweet_timestamp': '01-02-2021 09:00:10 UTC'}

JSON_100_WORD_CLOUD = {
    'words': ['advance', 'aged', 'amp', 'an', 'and', 'anyone', 'ap', 'appoinment', 'are', 'as', 'be', 'beat', 'book',
              'booking', 'brace', 'city', 'colleagues', 'coming', 'coronavirus', 'could', 'covid',
              'criticalcareparamedic', 'details', 'do', 'expert', 'for', 'form', 'full', 'have', 'haven', 'health',
              'healthnews', 'heartattacks', 'here', 'how', 'humor', 'hurricane', 'impact', 'in', 'including',
              'incorporate', 'into', 'is', 'know', 'link', 'live', 'long', 'need', 'news', 'no', 'northeastlondon',
              'now', 'of', 'on', 'online', 'our', 'pa', 'predicted', 'received', 'restrictions', 'resulted',
              'retrieval', 'revival', 'says', 'sex', 'show', 'simple', 'some', 'storyline', 'strain', 'tackle',
              'tasked', 'team', 'that', 'the', 'their', 'this', 'time', 'to', 'tune', 'up', 'us', 'vaccination',
              'virulent', 'visit', 'wait', 'warns', 'wellnessiq', 'were', 'who', 'will', 'wion', 'wionnews', 'with',
              'working', 'xray', 'year', 'yet', 'you', 'your'],
    'topic': 'covid',
    'first_tweet_timestamp': '01-02-2021 09:00:00 UTC',
    'last_tweet_timestamp': '01-02-2021 09:00:10 UTC'}
