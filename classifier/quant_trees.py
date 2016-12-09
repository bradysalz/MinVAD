def tree_16b(features):
  if features[12] <= 0.0026689696301218646:
    if features[2] <= 0.00825153129312639:
      if features[19] <= 0.005966400067336508:
        if features[19] <= 0.0029812112336458085:
          if features[17] <= 0.001915214421615019:
            return 0
          else:  # if features[17] > 0.001915214421615019
            return 0
        else:  # if features[19] > 0.0029812112336458085
          if features[2] <= 0.0018615168210089905:
            return 0
          else:  # if features[2] > 0.0018615168210089905
            return 0
      else:  # if features[19] > 0.005966400067336508
        if features[19] <= 0.00793332328953511:
          if features[18] <= 0.005491076861972033:
            return 1
          else:  # if features[18] > 0.005491076861972033
            return 0
        else:  # if features[19] > 0.00793332328953511
          if features[6] <= 0.001075940812143017:
            return 1
          else:  # if features[6] > 0.001075940812143017
            return 1
    else:  # if features[2] > 0.00825153129312639
      if features[2] <= 0.011165123326009052:
        if features[19] <= 0.0012947088146120223:
          if features[9] <= 0.002559585628887362:
            return 1
          else:  # if features[9] > 0.002559585628887362
            return 0
        else:  # if features[19] > 0.0012947088146120223
          if features[10] <= 0.0028857488325684244:
            return 1
          else:  # if features[10] > 0.0028857488325684244
            return 0
      else:  # if features[2] > 0.011165123326009052
        if features[1] <= 0.012951065746165114:
          if features[6] <= 0.009407024106167228:
            return 1
          else:  # if features[6] > 0.009407024106167228
            return 0
        else:  # if features[1] > 0.012951065746165114
          return 1
  else:  # if features[12] > 0.0026689696301218646
    if features[19] <= 0.017378134596128803:
      if features[2] <= 0.01920186421671133:
        if features[0] <= 0.0018734496211436635:
          if features[10] <= 0.0055686400628474075:
            return 0
          else:  # if features[10] > 0.0055686400628474075
            return 1
        else:  # if features[0] > 0.0018734496211436635
          if features[3] <= 0.02158046904355615:
            return 0
          else:  # if features[3] > 0.02158046904355615
            return 1
      else:  # if features[2] > 0.01920186421671133
        if features[3] <= 0.06516701033547179:
          if features[15] <= 0.00476715365380187:
            return 1
          else:  # if features[15] > 0.00476715365380187
            return 1
        else:  # if features[3] > 0.06516701033547179
          if features[0] <= 0.034261057986668675:
            return 1
          else:  # if features[0] > 0.034261057986668675
            return 0
    else:  # if features[19] > 0.017378134596128803
      if features[0] <= 0.0035281312398183218:
        if features[2] <= 0.0026570368299871916:
          if features[14] <= 0.008929712100780307:
            return 1
          else:  # if features[14] > 0.008929712100780307
            return 0
        else:  # if features[2] > 0.0026570368299871916
          if features[19] <= 0.03522761479757719:
            return 1
          else:  # if features[19] > 0.03522761479757719
            return 0
      else:  # if features[0] > 0.0035281312398183218
        if features[8] <= 0.0518500053851767:
          if features[13] <= 0.010222432115369884:
            return 1
          else:  # if features[13] > 0.010222432115369884
            return 0
        else:  # if features[8] > 0.0518500053851767
          if features[0] <= 0.03477615719248206:
            return 1
          else:  # if features[0] > 0.03477615719248206
            return 0
##################################################
def tree_15b(features):
  if features[12] <= 0.0026689696301218646:
    if features[2] <= 0.008249542493103945:
      if features[19] <= 0.005966400067336508:
        if features[19] <= 0.002979222433623363:
          if features[17] <= 0.0019132256215925736:
            return 0
          else:  # if features[17] > 0.0019132256215925736
            return 0
        else:  # if features[19] > 0.002979222433623363
          if features[2] <= 0.0018615168210089905:
            return 0
          else:  # if features[2] > 0.0018615168210089905
            return 0
      else:  # if features[19] > 0.005966400067336508
        if features[19] <= 0.007935312089557556:
          if features[18] <= 0.005493065661994478:
            return 1
          else:  # if features[18] > 0.005493065661994478
            return 0
        else:  # if features[19] > 0.007935312089557556
          if features[6] <= 0.0010739520121205715:
            return 1
          else:  # if features[6] > 0.0010739520121205715
            return 1
    else:  # if features[2] > 0.008249542493103945
      if features[2] <= 0.011165123326009052:
        if features[19] <= 0.0012927200145895767:
          if features[9] <= 0.0025575968288649165:
            return 1
          else:  # if features[9] > 0.0025575968288649165
            return 0
        else:  # if features[19] > 0.0012927200145895767
          if features[10] <= 0.00288773763259087:
            return 1
          else:  # if features[10] > 0.00288773763259087
            return 0
      else:  # if features[2] > 0.011165123326009052
        if features[1] <= 0.012951065746165114:
          if features[6] <= 0.009407024106167228:
            return 1
          else:  # if features[6] > 0.009407024106167228
            return 0
        else:  # if features[1] > 0.012951065746165114
          return 1
  else:  # if features[12] > 0.0026689696301218646
    if features[19] <= 0.017378134596128803:
      if features[2] <= 0.019199875416688883:
        if features[0] <= 0.0018734496211436635:
          if features[10] <= 0.0055686400628474075:
            return 0
          else:  # if features[10] > 0.0055686400628474075
            return 1
        else:  # if features[0] > 0.0018734496211436635
          if features[3] <= 0.021582457843578595:
            return 0
          else:  # if features[3] > 0.021582457843578595
            return 1
      else:  # if features[2] > 0.019199875416688883
        if features[3] <= 0.06516502153544934:
          if features[15] <= 0.0047651648537794244:
            return 1
          else:  # if features[15] > 0.0047651648537794244
            return 1
        else:  # if features[3] > 0.06516502153544934
          if features[0] <= 0.03426304678669112:
            return 1
          else:  # if features[0] > 0.03426304678669112
            return 0
    else:  # if features[19] > 0.017378134596128803
      if features[0] <= 0.0035281312398183218:
        if features[2] <= 0.0026570368299871916:
          if features[14] <= 0.008929712100780307:
            return 1
          else:  # if features[14] > 0.008929712100780307
            return 0
        else:  # if features[2] > 0.0026570368299871916
          if features[19] <= 0.035225625997554744:
            return 1
          else:  # if features[19] > 0.035225625997554744
            return 0
      else:  # if features[0] > 0.0035281312398183218
        if features[8] <= 0.051848016585154255:
          if features[13] <= 0.010222432115369884:
            return 1
          else:  # if features[13] > 0.010222432115369884
            return 0
        else:  # if features[8] > 0.051848016585154255
          if features[0] <= 0.03477615719248206:
            return 1
          else:  # if features[0] > 0.03477615719248206
            return 0
##################################################
def tree_14b(features):
  if features[12] <= 0.0026729472301667556:
    if features[2] <= 0.008249542493103945:
      if features[19] <= 0.005966400067336508:
        if features[19] <= 0.002983200033668254:
          if features[17] <= 0.0019172032216374646:
            return 0
          else:  # if features[17] > 0.0019172032216374646
            return 0
        else:  # if features[19] > 0.002983200033668254
          if features[2] <= 0.0018615168210089905:
            return 0
          else:  # if features[2] > 0.0018615168210089905
            return 0
      else:  # if features[19] > 0.005966400067336508
        if features[19] <= 0.007931334489512665:
          if features[18] <= 0.005489088061949587:
            return 1
          else:  # if features[18] > 0.005489088061949587
            return 0
        else:  # if features[19] > 0.007931334489512665
          if features[6] <= 0.0010739520121205715:
            return 1
          else:  # if features[6] > 0.0010739520121205715
            return 1
    else:  # if features[2] > 0.008249542493103945
      if features[2] <= 0.011161145725964161:
        if features[19] <= 0.0012966976146344678:
          if features[9] <= 0.0025615744289098075:
            return 1
          else:  # if features[9] > 0.0025615744289098075
            return 0
        else:  # if features[19] > 0.0012966976146344678
          if features[10] <= 0.00288773763259087:
            return 1
          else:  # if features[10] > 0.00288773763259087
            return 0
      else:  # if features[2] > 0.011161145725964161
        if features[1] <= 0.012951065746165114:
          if features[6] <= 0.009411001706212119:
            return 1
          else:  # if features[6] > 0.009411001706212119
            return 0
        else:  # if features[1] > 0.012951065746165114
          return 1
  else:  # if features[12] > 0.0026729472301667556
    if features[19] <= 0.01737415699608391:
      if features[2] <= 0.019203853016733774:
        if features[0] <= 0.0018774272211885545:
          if features[10] <= 0.0055686400628474075:
            return 0
          else:  # if features[10] > 0.0055686400628474075
            return 1
        else:  # if features[0] > 0.0018774272211885545
          if features[3] <= 0.021582457843578595:
            return 0
          else:  # if features[3] > 0.021582457843578595
            return 1
      else:  # if features[2] > 0.019203853016733774
        if features[3] <= 0.06516104393540445:
          if features[15] <= 0.0047651648537794244:
            return 1
          else:  # if features[15] > 0.0047651648537794244
            return 1
        else:  # if features[3] > 0.06516104393540445
          if features[0] <= 0.03426304678669112:
            return 1
          else:  # if features[0] > 0.03426304678669112
            return 0
    else:  # if features[19] > 0.01737415699608391
      if features[0] <= 0.0035321088398632128:
        if features[2] <= 0.0026570368299871916:
          if features[14] <= 0.008925734500735416:
            return 1
          else:  # if features[14] > 0.008925734500735416
            return 0
        else:  # if features[2] > 0.0026570368299871916
          if features[19] <= 0.035225625997554744:
            return 1
          else:  # if features[19] > 0.035225625997554744
            return 0
      else:  # if features[0] > 0.0035321088398632128
        if features[8] <= 0.051851994185199146:
          if features[13] <= 0.010222432115369884:
            return 1
          else:  # if features[13] > 0.010222432115369884
            return 0
        else:  # if features[8] > 0.051851994185199146
          if features[0] <= 0.03477217959243717:
            return 1
          else:  # if features[0] > 0.03477217959243717
            return 0
##################################################
def tree_13b(features):
  if features[12] <= 0.0026729472301667556:
    if features[2] <= 0.008257497693193727:
      if features[19] <= 0.005966400067336508:
        if features[19] <= 0.002975244833578472:
          if features[17] <= 0.0019092480215476826:
            return 0
          else:  # if features[17] > 0.0019092480215476826
            return 0
        else:  # if features[19] > 0.002975244833578472
          if features[2] <= 0.0018615168210089905:
            return 0
          else:  # if features[2] > 0.0018615168210089905
            return 0
      else:  # if features[19] > 0.005966400067336508
        if features[19] <= 0.007939289689602447:
          if features[18] <= 0.005489088061949587:
            return 1
          else:  # if features[18] > 0.005489088061949587
            return 0
        else:  # if features[19] > 0.007939289689602447
          if features[6] <= 0.0010819072122103535:
            return 1
          else:  # if features[6] > 0.0010819072122103535
            return 1
    else:  # if features[2] > 0.008257497693193727
      if features[2] <= 0.011169100926053943:
        if features[19] <= 0.0012887424145446857:
          if features[9] <= 0.0025615744289098075:
            return 1
          else:  # if features[9] > 0.0025615744289098075
            return 0
        else:  # if features[19] > 0.0012887424145446857
          if features[10] <= 0.002879782432501088:
            return 1
          else:  # if features[10] > 0.002879782432501088
            return 0
      else:  # if features[2] > 0.011169100926053943
        if features[1] <= 0.012951065746165114:
          if features[6] <= 0.009403046506122337:
            return 1
          else:  # if features[6] > 0.009403046506122337
            return 0
        else:  # if features[1] > 0.012951065746165114
          return 1
  else:  # if features[12] > 0.0026729472301667556
    if features[19] <= 0.01737415699608391:
      if features[2] <= 0.019203853016733774:
        if features[0] <= 0.0018774272211885545:
          if features[10] <= 0.0055686400628474075:
            return 0
          else:  # if features[10] > 0.0055686400628474075
            return 1
        else:  # if features[0] > 0.0018774272211885545
          if features[3] <= 0.021574502643488813:
            return 0
          else:  # if features[3] > 0.021574502643488813
            return 1
      else:  # if features[2] > 0.019203853016733774
        if features[3] <= 0.06515308873531467:
          if features[15] <= 0.0047731200538692065:
            return 1
          else:  # if features[15] > 0.0047731200538692065
            return 1
        else:  # if features[3] > 0.06515308873531467
          if features[0] <= 0.03425509158660134:
            return 1
          else:  # if features[0] > 0.03425509158660134
            return 0
    else:  # if features[19] > 0.01737415699608391
      if features[0] <= 0.0035321088398632128:
        if features[2] <= 0.0026570368299871916:
          if features[14] <= 0.008925734500735416:
            return 1
          else:  # if features[14] > 0.008925734500735416
            return 0
        else:  # if features[2] > 0.0026570368299871916
          if features[19] <= 0.035225625997554744:
            return 1
          else:  # if features[19] > 0.035225625997554744
            return 0
      else:  # if features[0] > 0.0035321088398632128
        if features[8] <= 0.051851994185199146:
          if features[13] <= 0.010214476915280102:
            return 1
          else:  # if features[13] > 0.010214476915280102
            return 0
        else:  # if features[8] > 0.051851994185199146
          if features[0] <= 0.03478013479252695:
            return 1
          else:  # if features[0] > 0.03478013479252695
            return 0
##################################################
def tree_12b(features):
  if features[12] <= 0.0026729472301667556:
    if features[2] <= 0.008241587293014163:
      if features[19] <= 0.005950489667156944:
        if features[19] <= 0.002991155233758036:
          if features[17] <= 0.0019092480215476826:
            return 0
          else:  # if features[17] > 0.0019092480215476826
            return 0
        else:  # if features[19] > 0.002991155233758036
          if features[2] <= 0.0018456064208294265:
            return 0
          else:  # if features[2] > 0.0018456064208294265
            return 0
      else:  # if features[19] > 0.005950489667156944
        if features[19] <= 0.007923379289422883:
          if features[18] <= 0.0055049984621291514:
            return 1
          else:  # if features[18] > 0.0055049984621291514
            return 0
        else:  # if features[19] > 0.007923379289422883
          if features[6] <= 0.0010819072122103535:
            return 1
          else:  # if features[6] > 0.0010819072122103535
            return 1
    else:  # if features[2] > 0.008241587293014163
      if features[2] <= 0.011169100926053943:
        if features[19] <= 0.0013046528147242498:
          if features[9] <= 0.0025456640287302434:
            return 1
          else:  # if features[9] > 0.0025456640287302434
            return 0
        else:  # if features[19] > 0.0013046528147242498
          if features[10] <= 0.002895692832680652:
            return 1
          else:  # if features[10] > 0.002895692832680652
            return 0
      else:  # if features[2] > 0.011169100926053943
        if features[1] <= 0.012951065746165114:
          if features[6] <= 0.0094189569063019:
            return 1
          else:  # if features[6] > 0.0094189569063019
            return 0
        else:  # if features[1] > 0.012951065746165114
          return 1
  else:  # if features[12] > 0.0026729472301667556
    if features[19] <= 0.01737415699608391:
      if features[2] <= 0.01918794261655421:
        if features[0] <= 0.0018774272211885545:
          if features[10] <= 0.0055686400628474075:
            return 0
          else:  # if features[10] > 0.0055686400628474075
            return 1
        else:  # if features[0] > 0.0018774272211885545
          if features[3] <= 0.021574502643488813:
            return 0
          else:  # if features[3] > 0.021574502643488813
            return 1
      else:  # if features[2] > 0.01918794261655421
        if features[3] <= 0.0651371783351351:
          if features[15] <= 0.0047731200538692065:
            return 1
          else:  # if features[15] > 0.0047731200538692065
            return 1
        else:  # if features[3] > 0.0651371783351351
          if features[0] <= 0.0342710019867809:
            return 1
          else:  # if features[0] > 0.0342710019867809
            return 0
    else:  # if features[19] > 0.01737415699608391
      if features[0] <= 0.0035321088398632128:
        if features[2] <= 0.0026411264298076276:
          if features[14] <= 0.00894164490091498:
            return 1
          else:  # if features[14] > 0.00894164490091498
            return 0
        else:  # if features[2] > 0.0026411264298076276
          if features[19] <= 0.035225625997554744:
            return 1
          else:  # if features[19] > 0.035225625997554744
            return 0
      else:  # if features[0] > 0.0035321088398632128
        if features[8] <= 0.05183608378501958:
          if features[13] <= 0.010214476915280102:
            return 1
          else:  # if features[13] > 0.010214476915280102
            return 0
        else:  # if features[8] > 0.05183608378501958
          if features[0] <= 0.03478013479252695:
            return 1
          else:  # if features[0] > 0.03478013479252695
            return 0
##################################################
def tree_11b(features):
  if features[12] <= 0.0026729472301667556:
    if features[2] <= 0.008273408093373291:
      if features[19] <= 0.005982310467516072:
        if features[19] <= 0.002991155233758036:
          if features[17] <= 0.0019092480215476826:
            return 0
          else:  # if features[17] > 0.0019092480215476826
            return 0
        else:  # if features[19] > 0.002991155233758036
          if features[2] <= 0.0018456064208294265:
            return 0
          else:  # if features[2] > 0.0018456064208294265
            return 0
      else:  # if features[19] > 0.005982310467516072
        if features[19] <= 0.00795520008978201:
          if features[18] <= 0.005473177661770023:
            return 1
          else:  # if features[18] > 0.005473177661770023
            return 0
        else:  # if features[19] > 0.00795520008978201
          if features[6] <= 0.0010819072122103535:
            return 1
          else:  # if features[6] > 0.0010819072122103535
            return 1
    else:  # if features[2] > 0.008273408093373291
      if features[2] <= 0.011137280125694815:
        if features[19] <= 0.0012728320143651217:
          if features[9] <= 0.0025456640287302434:
            return 1
          else:  # if features[9] > 0.0025456640287302434
            return 0
        else:  # if features[19] > 0.0012728320143651217
          if features[10] <= 0.002863872032321524:
            return 1
          else:  # if features[10] > 0.002863872032321524
            return 0
      else:  # if features[2] > 0.011137280125694815
        if features[1] <= 0.012919244945805985:
          if features[6] <= 0.0094189569063019:
            return 1
          else:  # if features[6] > 0.0094189569063019
            return 0
        else:  # if features[1] > 0.012919244945805985
          return 1
  else:  # if features[12] > 0.0026729472301667556
    if features[19] <= 0.01737415699608391:
      if features[2] <= 0.019219763416913338:
        if features[0] <= 0.0018456064208294265:
          if features[10] <= 0.0055368192624882795:
            return 0
          else:  # if features[10] > 0.0055368192624882795
            return 1
        else:  # if features[0] > 0.0018456064208294265
          if features[3] <= 0.021574502643488813:
            return 0
          else:  # if features[3] > 0.021574502643488813
            return 1
      else:  # if features[2] > 0.019219763416913338
        if features[3] <= 0.06510535753477598:
          if features[15] <= 0.0047731200538692065:
            return 1
          else:  # if features[15] > 0.0047731200538692065
            return 1
        else:  # if features[3] > 0.06510535753477598
          if features[0] <= 0.034239181186421774:
            return 1
          else:  # if features[0] > 0.034239181186421774
            return 0
    else:  # if features[19] > 0.01737415699608391
      if features[0] <= 0.0035002880395040847:
        if features[2] <= 0.0026729472301667556:
          if features[14] <= 0.008909824100555852:
            return 1
          else:  # if features[14] > 0.008909824100555852
            return 0
        else:  # if features[2] > 0.0026729472301667556
          if features[19] <= 0.03525744679791387:
            return 1
          else:  # if features[19] > 0.03525744679791387
            return 0
      else:  # if features[0] > 0.0035002880395040847
        if features[8] <= 0.05186790458537871:
          if features[13] <= 0.01024629771563923:
            return 1
          else:  # if features[13] > 0.01024629771563923
            return 0
        else:  # if features[8] > 0.05186790458537871
          if features[0] <= 0.03474831399216782:
            return 1
          else:  # if features[0] > 0.03474831399216782
            return 0
##################################################
def tree_10b(features):
  if features[12] <= 0.0026729472301667556:
    if features[2] <= 0.008273408093373291:
      if features[19] <= 0.005982310467516072:
        if features[19] <= 0.00292751363303978:
          if features[17] <= 0.0019092480215476826:
            return 0
          else:  # if features[17] > 0.0019092480215476826
            return 0
        else:  # if features[19] > 0.00292751363303978
          if features[2] <= 0.0019092480215476826:
            return 0
          else:  # if features[2] > 0.0019092480215476826
            return 0
      else:  # if features[19] > 0.005982310467516072
        if features[19] <= 0.007891558489063755:
          if features[18] <= 0.005473177661770023:
            return 1
          else:  # if features[18] > 0.005473177661770023
            return 0
        else:  # if features[19] > 0.007891558489063755
          if features[6] <= 0.0010182656114920974:
            return 1
          else:  # if features[6] > 0.0010182656114920974
            return 1
    else:  # if features[2] > 0.008273408093373291
      if features[2] <= 0.011200921726413071:
        if features[19] <= 0.0012728320143651217:
          if features[9] <= 0.0025456640287302434:
            return 1
          else:  # if features[9] > 0.0025456640287302434
            return 0
        else:  # if features[19] > 0.0012728320143651217
          if features[10] <= 0.00292751363303978:
            return 1
          else:  # if features[10] > 0.00292751363303978
            return 0
      else:  # if features[2] > 0.011200921726413071
        if features[1] <= 0.012982886546524242:
          if features[6] <= 0.0094189569063019:
            return 1
          else:  # if features[6] > 0.0094189569063019
            return 0
        else:  # if features[1] > 0.012982886546524242
          return 1
  else:  # if features[12] > 0.0026729472301667556
    if features[19] <= 0.017437798596802168:
      if features[2] <= 0.019219763416913338:
        if features[0] <= 0.0019092480215476826:
          if features[10] <= 0.005600460863206536:
            return 0
          else:  # if features[10] > 0.005600460863206536
            return 1
        else:  # if features[0] > 0.0019092480215476826
          if features[3] <= 0.02163814424420707:
            return 0
          else:  # if features[3] > 0.02163814424420707
            return 1
      else:  # if features[2] > 0.019219763416913338
        if features[3] <= 0.06504171593405772:
          if features[15] <= 0.00470947845315095:
            return 1
          else:  # if features[15] > 0.00470947845315095
            return 1
        else:  # if features[3] > 0.06504171593405772
          if features[0] <= 0.034239181186421774:
            return 1
          else:  # if features[0] > 0.034239181186421774
            return 0
    else:  # if features[19] > 0.017437798596802168
      if features[0] <= 0.003563929640222341:
        if features[2] <= 0.0026729472301667556:
          if features[14] <= 0.008909824100555852:
            return 1
          else:  # if features[14] > 0.008909824100555852
            return 0
        else:  # if features[2] > 0.0026729472301667556
          if features[19] <= 0.03525744679791387:
            return 1
          else:  # if features[19] > 0.03525744679791387
            return 0
      else:  # if features[0] > 0.003563929640222341
        if features[8] <= 0.051804262984660454:
          if features[13] <= 0.010182656114920974:
            return 1
          else:  # if features[13] > 0.010182656114920974
            return 0
        else:  # if features[8] > 0.051804262984660454
          if features[0] <= 0.03474831399216782:
            return 1
          else:  # if features[0] > 0.03474831399216782
            return 0
##################################################
def tree_9b(features):
  if features[12] <= 0.0025456640287302434:
    if features[2] <= 0.008146124891936779:
      if features[19] <= 0.00585502726607956:
        if features[19] <= 0.003054796834476292:
          if features[17] <= 0.0020365312229841948:
            return 0
          else:  # if features[17] > 0.0020365312229841948
            return 0
        else:  # if features[19] > 0.003054796834476292
          if features[2] <= 0.0017819648201111704:
            return 0
          else:  # if features[2] > 0.0017819648201111704
            return 0
      else:  # if features[19] > 0.00585502726607956
        if features[19] <= 0.007891558489063755:
          if features[18] <= 0.005600460863206536:
            return 1
          else:  # if features[18] > 0.005600460863206536
            return 0
        else:  # if features[19] > 0.007891558489063755
          if features[6] <= 0.0010182656114920974:
            return 1
          else:  # if features[6] > 0.0010182656114920974
            return 1
    else:  # if features[2] > 0.008146124891936779
      if features[2] <= 0.011200921726413071:
        if features[19] <= 0.0012728320143651217:
          if features[9] <= 0.0025456640287302434:
            return 1
          else:  # if features[9] > 0.0025456640287302434
            return 0
        else:  # if features[19] > 0.0012728320143651217
          if features[10] <= 0.002800230431603268:
            return 1
          else:  # if features[10] > 0.002800230431603268
            return 0
      else:  # if features[2] > 0.011200921726413071
        if features[1] <= 0.012982886546524242:
          if features[6] <= 0.0094189569063019:
            return 1
          else:  # if features[6] > 0.0094189569063019
            return 0
        else:  # if features[1] > 0.012982886546524242
          return 1
  else:  # if features[12] > 0.0025456640287302434
    if features[19] <= 0.017310515395365655:
      if features[2] <= 0.019092480215476826:
        if features[0] <= 0.0017819648201111704:
          if features[10] <= 0.005600460863206536:
            return 0
          else:  # if features[10] > 0.005600460863206536
            return 1
        else:  # if features[0] > 0.0017819648201111704
          if features[3] <= 0.02163814424420707:
            return 0
          else:  # if features[3] > 0.02163814424420707
            return 1
      else:  # if features[2] > 0.019092480215476826
        if features[3] <= 0.06491443273262121:
          if features[15] <= 0.0048367616545874625:
            return 1
          else:  # if features[15] > 0.0048367616545874625
            return 1
        else:  # if features[3] > 0.06491443273262121
          if features[0] <= 0.034366464387858286:
            return 1
          else:  # if features[0] > 0.034366464387858286
            return 0
    else:  # if features[19] > 0.017310515395365655
      if features[0] <= 0.003563929640222341:
        if features[2] <= 0.0025456640287302434:
          if features[14] <= 0.008909824100555852:
            return 1
          else:  # if features[14] > 0.008909824100555852
            return 0
        else:  # if features[2] > 0.0025456640287302434
          if features[19] <= 0.03513016359647736:
            return 1
          else:  # if features[19] > 0.03513016359647736
            return 0
      else:  # if features[0] > 0.003563929640222341
        if features[8] <= 0.051931546186096966:
          if features[13] <= 0.010182656114920974:
            return 1
          else:  # if features[13] > 0.010182656114920974
            return 0
        else:  # if features[8] > 0.051931546186096966
          if features[0] <= 0.034875597193604335:
            return 1
          else:  # if features[0] > 0.034875597193604335
            return 0
##################################################
def tree_8b(features):
  if features[12] <= 0.0025456640287302434:
    if features[2] <= 0.008146124891936779:
      if features[19] <= 0.006109593668952584:
        if features[19] <= 0.003054796834476292:
          if features[17] <= 0.0020365312229841948:
            return 0
          else:  # if features[17] > 0.0020365312229841948
            return 0
        else:  # if features[19] > 0.003054796834476292
          if features[2] <= 0.0020365312229841948:
            return 0
          else:  # if features[2] > 0.0020365312229841948
            return 0
      else:  # if features[19] > 0.006109593668952584
        if features[19] <= 0.008146124891936779:
          if features[18] <= 0.005600460863206536:
            return 1
          else:  # if features[18] > 0.005600460863206536
            return 0
        else:  # if features[19] > 0.008146124891936779
          if features[6] <= 0.0010182656114920974:
            return 1
          else:  # if features[6] > 0.0010182656114920974
            return 1
    else:  # if features[2] > 0.008146124891936779
      if features[2] <= 0.011200921726413071:
        if features[19] <= 0.001527398417238146:
          if features[9] <= 0.0025456640287302434:
            return 1
          else:  # if features[9] > 0.0025456640287302434
            return 0
        else:  # if features[19] > 0.001527398417238146
          if features[10] <= 0.003054796834476292:
            return 1
          else:  # if features[10] > 0.003054796834476292
            return 0
      else:  # if features[2] > 0.011200921726413071
        if features[1] <= 0.012728320143651217:
          if features[6] <= 0.009164390503428876:
            return 1
          else:  # if features[6] > 0.009164390503428876
            return 0
        else:  # if features[1] > 0.012728320143651217
          return 1
  else:  # if features[12] > 0.0025456640287302434
    if features[19] <= 0.017310515395365655:
      if features[2] <= 0.01934704661834985:
        if features[0] <= 0.0020365312229841948:
          if features[10] <= 0.005600460863206536:
            return 0
          else:  # if features[10] > 0.005600460863206536
            return 1
        else:  # if features[0] > 0.0020365312229841948
          if features[3] <= 0.021383577841334045:
            return 0
          else:  # if features[3] > 0.021383577841334045
            return 1
      else:  # if features[2] > 0.01934704661834985
        if features[3] <= 0.06465986632974818:
          if features[15] <= 0.004582195251714438:
            return 1
          else:  # if features[15] > 0.004582195251714438
            return 1
        else:  # if features[3] > 0.06465986632974818
          if features[0] <= 0.03411189798498526:
            return 1
          else:  # if features[0] > 0.03411189798498526
            return 0
    else:  # if features[19] > 0.017310515395365655
      if features[0] <= 0.003563929640222341:
        if features[2] <= 0.0025456640287302434:
          if features[14] <= 0.009164390503428876:
            return 1
          else:  # if features[14] > 0.009164390503428876
            return 0
        else:  # if features[2] > 0.0025456640287302434
          if features[19] <= 0.03513016359647736:
            return 1
          else:  # if features[19] > 0.03513016359647736
            return 0
      else:  # if features[0] > 0.003563929640222341
        if features[8] <= 0.051931546186096966:
          if features[13] <= 0.010182656114920974:
            return 1
          else:  # if features[13] > 0.010182656114920974
            return 0
        else:  # if features[8] > 0.051931546186096966
          if features[0] <= 0.03462103079073131:
            return 1
          else:  # if features[0] > 0.03462103079073131
            return 0
##################################################
def tree_7b(features):
  if features[12] <= 0.003054796834476292:
    if features[2] <= 0.008146124891936779:
      if features[19] <= 0.006109593668952584:
        if features[19] <= 0.003054796834476292:
          if features[17] <= 0.0020365312229841948:
            return 0
          else:  # if features[17] > 0.0020365312229841948
            return 0
        else:  # if features[19] > 0.003054796834476292
          if features[2] <= 0.0020365312229841948:
            return 0
          else:  # if features[2] > 0.0020365312229841948
            return 0
      else:  # if features[19] > 0.006109593668952584
        if features[19] <= 0.008146124891936779:
          if features[18] <= 0.005091328057460487:
            return 1
          else:  # if features[18] > 0.005091328057460487
            return 0
        else:  # if features[19] > 0.008146124891936779
          if features[6] <= 0.0010182656114920974:
            return 1
          else:  # if features[6] > 0.0010182656114920974
            return 1
    else:  # if features[2] > 0.008146124891936779
      if features[2] <= 0.011200921726413071:
        if features[19] <= 0.0010182656114920974:
          if features[9] <= 0.003054796834476292:
            return 1
          else:  # if features[9] > 0.003054796834476292
            return 0
        else:  # if features[19] > 0.0010182656114920974
          if features[10] <= 0.003054796834476292:
            return 1
          else:  # if features[10] > 0.003054796834476292
            return 0
      else:  # if features[2] > 0.011200921726413071
        if features[1] <= 0.013237452949397266:
          if features[6] <= 0.009164390503428876:
            return 1
          else:  # if features[6] > 0.009164390503428876
            return 0
        else:  # if features[1] > 0.013237452949397266
          return 1
  else:  # if features[12] > 0.003054796834476292
    if features[19] <= 0.017310515395365655:
      if features[2] <= 0.01934704661834985:
        if features[0] <= 0.0020365312229841948:
          if features[10] <= 0.005091328057460487:
            return 0
          else:  # if features[10] > 0.005091328057460487
            return 1
        else:  # if features[0] > 0.0020365312229841948
          if features[3] <= 0.021383577841334045:
            return 0
          else:  # if features[3] > 0.021383577841334045
            return 1
      else:  # if features[2] > 0.01934704661834985
        if features[3] <= 0.06415073352400213:
          if features[15] <= 0.005091328057460487:
            return 1
          else:  # if features[15] > 0.005091328057460487
            return 1
        else:  # if features[3] > 0.06415073352400213
          if features[0] <= 0.03462103079073131:
            return 1
          else:  # if features[0] > 0.03462103079073131
            return 0
    else:  # if features[19] > 0.017310515395365655
      if features[0] <= 0.003054796834476292:
        if features[2] <= 0.003054796834476292:
          if features[14] <= 0.009164390503428876:
            return 1
          else:  # if features[14] > 0.009164390503428876
            return 0
        else:  # if features[2] > 0.003054796834476292
          if features[19] <= 0.03563929640222341:
            return 1
          else:  # if features[19] > 0.03563929640222341
            return 0
      else:  # if features[0] > 0.003054796834476292
        if features[8] <= 0.051931546186096966:
          if features[13] <= 0.010182656114920974:
            return 1
          else:  # if features[13] > 0.010182656114920974
            return 0
        else:  # if features[8] > 0.051931546186096966
          if features[0] <= 0.03462103079073131:
            return 1
          else:  # if features[0] > 0.03462103079073131
            return 0
##################################################
def tree_6b(features):
  if features[12] <= 0.0020365312229841948:
    if features[2] <= 0.008146124891936779:
      if features[19] <= 0.006109593668952584:
        if features[19] <= 0.0020365312229841948:
          if features[17] <= 0.0020365312229841948:
            return 0
          else:  # if features[17] > 0.0020365312229841948
            return 0
        else:  # if features[19] > 0.0020365312229841948
          if features[2] <= 0.0020365312229841948:
            return 0
          else:  # if features[2] > 0.0020365312229841948
            return 0
      else:  # if features[19] > 0.006109593668952584
        if features[19] <= 0.008146124891936779:
          if features[18] <= 0.006109593668952584:
            return 1
          else:  # if features[18] > 0.006109593668952584
            return 0
        else:  # if features[19] > 0.008146124891936779
          if features[6] <= 0.0020365312229841948:
            return 1
          else:  # if features[6] > 0.0020365312229841948
            return 1
    else:  # if features[2] > 0.008146124891936779
      if features[2] <= 0.010182656114920974:
        if features[19] <= 0.0020365312229841948:
          if features[9] <= 0.0020365312229841948:
            return 1
          else:  # if features[9] > 0.0020365312229841948
            return 0
        else:  # if features[19] > 0.0020365312229841948
          if features[10] <= 0.0020365312229841948:
            return 1
          else:  # if features[10] > 0.0020365312229841948
            return 0
      else:  # if features[2] > 0.010182656114920974
        if features[1] <= 0.012219187337905169:
          if features[6] <= 0.010182656114920974:
            return 1
          else:  # if features[6] > 0.010182656114920974
            return 0
        else:  # if features[1] > 0.012219187337905169
          return 1
  else:  # if features[12] > 0.0020365312229841948
    if features[19] <= 0.018328781006857753:
      if features[2] <= 0.018328781006857753:
        if features[0] <= 0.0020365312229841948:
          if features[10] <= 0.006109593668952584:
            return 0
          else:  # if features[10] > 0.006109593668952584
            return 1
        else:  # if features[0] > 0.0020365312229841948
          if features[3] <= 0.022401843452826142:
            return 0
          else:  # if features[3] > 0.022401843452826142
            return 1
      else:  # if features[2] > 0.018328781006857753
        if features[3] <= 0.06313246791251004:
          if features[15] <= 0.0040730624459683895:
            return 1
          else:  # if features[15] > 0.0040730624459683895
            return 1
        else:  # if features[3] > 0.06313246791251004
          if features[0] <= 0.03462103079073131:
            return 1
          else:  # if features[0] > 0.03462103079073131
            return 0
    else:  # if features[19] > 0.018328781006857753
      if features[0] <= 0.0040730624459683895:
        if features[2] <= 0.0020365312229841948:
          if features[14] <= 0.008146124891936779:
            return 1
          else:  # if features[14] > 0.008146124891936779
            return 0
        else:  # if features[2] > 0.0020365312229841948
          if features[19] <= 0.03462103079073131:
            return 1
          else:  # if features[19] > 0.03462103079073131
            return 0
      else:  # if features[0] > 0.0040730624459683895
        if features[8] <= 0.05091328057460487:
          if features[13] <= 0.010182656114920974:
            return 1
          else:  # if features[13] > 0.010182656114920974
            return 0
        else:  # if features[8] > 0.05091328057460487
          if features[0] <= 0.03462103079073131:
            return 1
          else:  # if features[0] > 0.03462103079073131
            return 0
##################################################
def tree_5b(features):
  if features[12] <= 0.0040730624459683895:
    if features[2] <= 0.008146124891936779:
      if features[19] <= 0.0040730624459683895:
        if features[19] <= 0.0040730624459683895:
          if features[17] <= 0.0:
            return 0
          else:  # if features[17] > 0.0
            return 0
        else:  # if features[19] > 0.0040730624459683895
          if features[2] <= 0.0:
            return 0
          else:  # if features[2] > 0.0
            return 0
      else:  # if features[19] > 0.0040730624459683895
        if features[19] <= 0.008146124891936779:
          if features[18] <= 0.0040730624459683895:
            return 1
          else:  # if features[18] > 0.0040730624459683895
            return 0
        else:  # if features[19] > 0.008146124891936779
          if features[6] <= 0.0:
            return 1
          else:  # if features[6] > 0.0
            return 1
    else:  # if features[2] > 0.008146124891936779
      if features[2] <= 0.012219187337905169:
        if features[19] <= 0.0:
          if features[9] <= 0.0040730624459683895:
            return 1
          else:  # if features[9] > 0.0040730624459683895
            return 0
        else:  # if features[19] > 0.0
          if features[10] <= 0.0040730624459683895:
            return 1
          else:  # if features[10] > 0.0040730624459683895
            return 0
      else:  # if features[2] > 0.012219187337905169
        if features[1] <= 0.012219187337905169:
          if features[6] <= 0.008146124891936779:
            return 1
          else:  # if features[6] > 0.008146124891936779
            return 0
        else:  # if features[1] > 0.012219187337905169
          return 1
  else:  # if features[12] > 0.0040730624459683895
    if features[19] <= 0.016292249783873558:
      if features[2] <= 0.020365312229841948:
        if features[0] <= 0.0:
          if features[10] <= 0.0040730624459683895:
            return 0
          else:  # if features[10] > 0.0040730624459683895
            return 1
        else:  # if features[0] > 0.0
          if features[3] <= 0.020365312229841948:
            return 0
          else:  # if features[3] > 0.020365312229841948
            return 1
      else:  # if features[2] > 0.020365312229841948
        if features[3] <= 0.06109593668952584:
          if features[15] <= 0.0040730624459683895:
            return 1
          else:  # if features[15] > 0.0040730624459683895
            return 1
        else:  # if features[3] > 0.06109593668952584
          if features[0] <= 0.032584499567747116:
            return 1
          else:  # if features[0] > 0.032584499567747116
            return 0
    else:  # if features[19] > 0.016292249783873558
      if features[0] <= 0.0040730624459683895:
        if features[2] <= 0.0040730624459683895:
          if features[14] <= 0.008146124891936779:
            return 1
          else:  # if features[14] > 0.008146124891936779
            return 0
        else:  # if features[2] > 0.0040730624459683895
          if features[19] <= 0.036657562013715506:
            return 1
          else:  # if features[19] > 0.036657562013715506
            return 0
      else:  # if features[0] > 0.0040730624459683895
        if features[8] <= 0.052949811797589064:
          if features[13] <= 0.012219187337905169:
            return 1
          else:  # if features[13] > 0.012219187337905169
            return 0
        else:  # if features[8] > 0.052949811797589064
          if features[0] <= 0.036657562013715506:
            return 1
          else:  # if features[0] > 0.036657562013715506
            return 0
##################################################
def tree_4b(features):
  if features[12] <= 0.0:
    if features[2] <= 0.008146124891936779:
      if features[19] <= 0.008146124891936779:
        if features[19] <= 0.0:
          if features[17] <= 0.0:
            return 0
          else:  # if features[17] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[2] <= 0.0:
            return 0
          else:  # if features[2] > 0.0
            return 0
      else:  # if features[19] > 0.008146124891936779
        if features[19] <= 0.008146124891936779:
          if features[18] <= 0.008146124891936779:
            return 1
          else:  # if features[18] > 0.008146124891936779
            return 0
        else:  # if features[19] > 0.008146124891936779
          if features[6] <= 0.0:
            return 1
          else:  # if features[6] > 0.0
            return 1
    else:  # if features[2] > 0.008146124891936779
      if features[2] <= 0.008146124891936779:
        if features[19] <= 0.0:
          if features[9] <= 0.0:
            return 1
          else:  # if features[9] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[10] <= 0.0:
            return 1
          else:  # if features[10] > 0.0
            return 0
      else:  # if features[2] > 0.008146124891936779
        if features[1] <= 0.016292249783873558:
          if features[6] <= 0.008146124891936779:
            return 1
          else:  # if features[6] > 0.008146124891936779
            return 0
        else:  # if features[1] > 0.016292249783873558
          return 1
  else:  # if features[12] > 0.0
    if features[19] <= 0.016292249783873558:
      if features[2] <= 0.016292249783873558:
        if features[0] <= 0.0:
          if features[10] <= 0.008146124891936779:
            return 0
          else:  # if features[10] > 0.008146124891936779
            return 1
        else:  # if features[0] > 0.0
          if features[3] <= 0.024438374675810337:
            return 0
          else:  # if features[3] > 0.024438374675810337
            return 1
      else:  # if features[2] > 0.016292249783873558
        if features[3] <= 0.05702287424355745:
          if features[15] <= 0.008146124891936779:
            return 1
          else:  # if features[15] > 0.008146124891936779
            return 1
        else:  # if features[3] > 0.05702287424355745
          if features[0] <= 0.032584499567747116:
            return 1
          else:  # if features[0] > 0.032584499567747116
            return 0
    else:  # if features[19] > 0.016292249783873558
      if features[0] <= 0.0:
        if features[2] <= 0.0:
          if features[14] <= 0.008146124891936779:
            return 1
          else:  # if features[14] > 0.008146124891936779
            return 0
        else:  # if features[2] > 0.0
          if features[19] <= 0.032584499567747116:
            return 1
          else:  # if features[19] > 0.032584499567747116
            return 0
      else:  # if features[0] > 0.0
        if features[8] <= 0.048876749351620674:
          if features[13] <= 0.008146124891936779:
            return 1
          else:  # if features[13] > 0.008146124891936779
            return 0
        else:  # if features[8] > 0.048876749351620674
          if features[0] <= 0.032584499567747116:
            return 1
          else:  # if features[0] > 0.032584499567747116
            return 0
##################################################
def tree_3b(features):
  if features[12] <= 0.0:
    if features[2] <= 0.016292249783873558:
      if features[19] <= 0.0:
        if features[19] <= 0.0:
          if features[17] <= 0.0:
            return 0
          else:  # if features[17] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[2] <= 0.0:
            return 0
          else:  # if features[2] > 0.0
            return 0
      else:  # if features[19] > 0.0
        if features[19] <= 0.0:
          if features[18] <= 0.0:
            return 1
          else:  # if features[18] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[6] <= 0.0:
            return 1
          else:  # if features[6] > 0.0
            return 1
    else:  # if features[2] > 0.016292249783873558
      if features[2] <= 0.016292249783873558:
        if features[19] <= 0.0:
          if features[9] <= 0.0:
            return 1
          else:  # if features[9] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[10] <= 0.0:
            return 1
          else:  # if features[10] > 0.0
            return 0
      else:  # if features[2] > 0.016292249783873558
        if features[1] <= 0.016292249783873558:
          if features[6] <= 0.016292249783873558:
            return 1
          else:  # if features[6] > 0.016292249783873558
            return 0
        else:  # if features[1] > 0.016292249783873558
          return 1
  else:  # if features[12] > 0.0
    if features[19] <= 0.016292249783873558:
      if features[2] <= 0.016292249783873558:
        if features[0] <= 0.0:
          if features[10] <= 0.0:
            return 0
          else:  # if features[10] > 0.0
            return 1
        else:  # if features[0] > 0.0
          if features[3] <= 0.016292249783873558:
            return 0
          else:  # if features[3] > 0.016292249783873558
            return 1
      else:  # if features[2] > 0.016292249783873558
        if features[3] <= 0.048876749351620674:
          if features[15] <= 0.0:
            return 1
          else:  # if features[15] > 0.0
            return 1
        else:  # if features[3] > 0.048876749351620674
          if features[0] <= 0.032584499567747116:
            return 1
          else:  # if features[0] > 0.032584499567747116
            return 0
    else:  # if features[19] > 0.016292249783873558
      if features[0] <= 0.0:
        if features[2] <= 0.0:
          if features[14] <= 0.016292249783873558:
            return 1
          else:  # if features[14] > 0.016292249783873558
            return 0
        else:  # if features[2] > 0.0
          if features[19] <= 0.032584499567747116:
            return 1
          else:  # if features[19] > 0.032584499567747116
            return 0
      else:  # if features[0] > 0.0
        if features[8] <= 0.048876749351620674:
          if features[13] <= 0.016292249783873558:
            return 1
          else:  # if features[13] > 0.016292249783873558
            return 0
        else:  # if features[8] > 0.048876749351620674
          if features[0] <= 0.032584499567747116:
            return 1
          else:  # if features[0] > 0.032584499567747116
            return 0
##################################################
def tree_2b(features):
  if features[12] <= 0.0:
    if features[2] <= 0.0:
      if features[19] <= 0.0:
        if features[19] <= 0.0:
          if features[17] <= 0.0:
            return 0
          else:  # if features[17] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[2] <= 0.0:
            return 0
          else:  # if features[2] > 0.0
            return 0
      else:  # if features[19] > 0.0
        if features[19] <= 0.0:
          if features[18] <= 0.0:
            return 1
          else:  # if features[18] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[6] <= 0.0:
            return 1
          else:  # if features[6] > 0.0
            return 1
    else:  # if features[2] > 0.0
      if features[2] <= 0.0:
        if features[19] <= 0.0:
          if features[9] <= 0.0:
            return 1
          else:  # if features[9] > 0.0
            return 0
        else:  # if features[19] > 0.0
          if features[10] <= 0.0:
            return 1
          else:  # if features[10] > 0.0
            return 0
      else:  # if features[2] > 0.0
        if features[1] <= 0.0:
          if features[6] <= 0.0:
            return 1
          else:  # if features[6] > 0.0
            return 0
        else:  # if features[1] > 0.0
          return 1
  else:  # if features[12] > 0.0
    if features[19] <= 0.032584499567747116:
      if features[2] <= 0.032584499567747116:
        if features[0] <= 0.0:
          if features[10] <= 0.0:
            return 0
          else:  # if features[10] > 0.0
            return 1
        else:  # if features[0] > 0.0
          if features[3] <= 0.032584499567747116:
            return 0
          else:  # if features[3] > 0.032584499567747116
            return 1
      else:  # if features[2] > 0.032584499567747116
        if features[3] <= 0.032584499567747116:
          if features[15] <= 0.0:
            return 1
          else:  # if features[15] > 0.0
            return 1
        else:  # if features[3] > 0.032584499567747116
          if features[0] <= 0.032584499567747116:
            return 1
          else:  # if features[0] > 0.032584499567747116
            return 0
    else:  # if features[19] > 0.032584499567747116
      if features[0] <= 0.0:
        if features[2] <= 0.0:
          if features[14] <= 0.0:
            return 1
          else:  # if features[14] > 0.0
            return 0
        else:  # if features[2] > 0.0
          if features[19] <= 0.032584499567747116:
            return 1
          else:  # if features[19] > 0.032584499567747116
            return 0
      else:  # if features[0] > 0.0
        if features[8] <= 0.032584499567747116:
          if features[13] <= 0.0:
            return 1
          else:  # if features[13] > 0.0
            return 0
        else:  # if features[8] > 0.032584499567747116
          if features[0] <= 0.032584499567747116:
            return 1
          else:  # if features[0] > 0.032584499567747116
            return 0
##################################################
