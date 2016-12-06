def tree_16b(features):
  if features[3] <= 0.022478051943835453:
    if features[7] <= 0.030786011746386066:
      if features[0] <= 0.034171463293205306:
        if features[11] <= 0.007646015672435169:
          if features[0] <= 0.03391341727638064:
            return 0
          else:  # if features[0] > 0.03391341727638064
            return 0
        else:  # if features[11] > 0.007646015672435169
          if features[1] <= 0.028213966122166312:
            return 0
          else:  # if features[1] > 0.028213966122166312
            return 0
      else:  # if features[0] > 0.034171463293205306
        if features[7] <= 0.009760871071193833:
          if features[15] <= 0.0021260747907945188:
            return 0
          else:  # if features[15] > 0.0021260747907945188
            return 0
        else:  # if features[7] > 0.009760871071193833
          if features[17] <= 0.005289943344905623:
            return 1
          else:  # if features[17] > 0.005289943344905623
            return 0
    else:  # if features[7] > 0.030786011746386066
      if features[19] <= 0.016111046963487752:
        if features[10] <= 0.019258086429545074:
          if features[5] <= 0.03197807215019566:
            return 0
          else:  # if features[5] > 0.03197807215019566
            return 1
        else:  # if features[10] > 0.019258086429545074
          if features[0] <= 0.0072449224071533536:
            return 0
          else:  # if features[0] > 0.0072449224071533536
            return 1
      else:  # if features[19] > 0.016111046963487752
        if features[14] <= 0.023333530586569395:
          return 1
        else:  # if features[14] > 0.023333530586569395
          if features[3] <= 0.022427564679674106:
            return 0
          else:  # if features[3] > 0.022427564679674106
            return 1
  else:  # if features[3] > 0.022478051943835453
    if features[7] <= 0.030651379041955806:
      if features[19] <= 0.005374088785174536:
        if features[1] <= 0.03206221759046457:
          if features[5] <= 0.027776409832767968:
            return 0
          else:  # if features[5] > 0.027776409832767968
            return 1
        else:  # if features[1] > 0.03206221759046457
          if features[7] <= 0.012658279064453382:
            return 0
          else:  # if features[7] > 0.012658279064453382
            return 1
      else:  # if features[19] > 0.005374088785174536
        if features[0] <= 0.015418249505273707:
          if features[6] <= 0.02533619206496951:
            return 0
          else:  # if features[6] > 0.02533619206496951
            return 1
        else:  # if features[0] > 0.015418249505273707
          if features[14] <= 0.006897121254041849:
            return 1
          else:  # if features[14] > 0.006897121254041849
            return 0
    else:  # if features[7] > 0.030651379041955806
      if features[19] <= 0.0327718441367324:
        if features[0] <= 0.09190645470971504:
          if features[3] <= 0.027061173590482213:
            return 1
          else:  # if features[3] > 0.027061173590482213
            return 1
        else:  # if features[0] > 0.09190645470971504
          return 0
      else:  # if features[19] > 0.0327718441367324
        if features[19] <= 0.04110785241937265:
          if features[17] <= 0.053404306090669706:
            return 0
          else:  # if features[17] > 0.053404306090669706
            return 1
        else:  # if features[19] > 0.04110785241937265
          if features[19] <= 0.04468683847881039:
            return 0
          else:  # if features[19] > 0.04468683847881039
            return 0
##################################################
def tree_15b(features):
  if features[3] <= 0.022478051943835453:
    if features[7] <= 0.030786011746386066:
      if features[0] <= 0.03416865844519634:
        if features[11] <= 0.007646015672435169:
          if features[0] <= 0.033916222124389606:
            return 0
          else:  # if features[0] > 0.033916222124389606
            return 0
        else:  # if features[11] > 0.007646015672435169
          if features[1] <= 0.028211161274157348:
            return 0
          else:  # if features[1] > 0.028211161274157348
            return 0
      else:  # if features[0] > 0.03416865844519634
        if features[7] <= 0.009760871071193833:
          if features[15] <= 0.0021260747907945188:
            return 0
          else:  # if features[15] > 0.0021260747907945188
            return 0
        else:  # if features[7] > 0.009760871071193833
          if features[17] <= 0.005289943344905623:
            return 1
          else:  # if features[17] > 0.005289943344905623
            return 0
    else:  # if features[7] > 0.030786011746386066
      if features[19] <= 0.016111046963487752:
        if features[10] <= 0.019258086429545074:
          if features[5] <= 0.031975267302186694:
            return 0
          else:  # if features[5] > 0.031975267302186694
            return 1
        else:  # if features[10] > 0.019258086429545074
          if features[0] <= 0.00724211755914439:
            return 0
          else:  # if features[0] > 0.00724211755914439
            return 1
      else:  # if features[19] > 0.016111046963487752
        if features[14] <= 0.02333633543457836:
          return 1
        else:  # if features[14] > 0.02333633543457836
          if features[3] <= 0.022427564679674106:
            return 0
          else:  # if features[3] > 0.022427564679674106
            return 1
  else:  # if features[3] > 0.022478051943835453
    if features[7] <= 0.030651379041955806:
      if features[19] <= 0.005374088785174536:
        if features[1] <= 0.032059412742455606:
          if features[5] <= 0.02777921468077693:
            return 0
          else:  # if features[5] > 0.02777921468077693
            return 1
        else:  # if features[1] > 0.032059412742455606
          if features[7] <= 0.012655474216444418:
            return 0
          else:  # if features[7] > 0.012655474216444418
            return 1
      else:  # if features[19] > 0.005374088785174536
        if features[0] <= 0.015415444657264743:
          if features[6] <= 0.025333387216960546:
            return 0
          else:  # if features[6] > 0.025333387216960546
            return 1
        else:  # if features[0] > 0.015415444657264743
          if features[14] <= 0.006899926102050813:
            return 1
          else:  # if features[14] > 0.006899926102050813
            return 0
    else:  # if features[7] > 0.030651379041955806
      if features[19] <= 0.0327718441367324:
        if features[0] <= 0.09190364986170607:
          if features[3] <= 0.027061173590482213:
            return 1
          else:  # if features[3] > 0.027061173590482213
            return 1
        else:  # if features[0] > 0.09190364986170607
          return 0
      else:  # if features[19] > 0.0327718441367324
        if features[19] <= 0.04110785241937265:
          if features[17] <= 0.053404306090669706:
            return 0
          else:  # if features[17] > 0.053404306090669706
            return 1
        else:  # if features[19] > 0.04110785241937265
          if features[19] <= 0.04468683847881039:
            return 0
          else:  # if features[19] > 0.04468683847881039
            return 0
##################################################
def tree_14b(features):
  if features[3] <= 0.022472442247817526:
    if features[7] <= 0.030786011746386066:
      if features[0] <= 0.03417426814121427:
        if features[11] <= 0.007640405976417242:
          if features[0] <= 0.033916222124389606:
            return 0
          else:  # if features[0] > 0.033916222124389606
            return 0
        else:  # if features[11] > 0.007640405976417242
          if features[1] <= 0.028216770970175276:
            return 0
          else:  # if features[1] > 0.028216770970175276
            return 0
      else:  # if features[0] > 0.03417426814121427
        if features[7] <= 0.009760871071193833:
          if features[15] <= 0.0021316844868124463:
            return 0
          else:  # if features[15] > 0.0021316844868124463
            return 0
        else:  # if features[7] > 0.009760871071193833
          if features[17] <= 0.005295553040923551:
            return 1
          else:  # if features[17] > 0.005295553040923551
            return 0
    else:  # if features[7] > 0.030786011746386066
      if features[19] <= 0.016111046963487752:
        if features[10] <= 0.019252476733527146:
          if features[5] <= 0.031975267302186694:
            return 0
          else:  # if features[5] > 0.031975267302186694
            return 1
        else:  # if features[10] > 0.019252476733527146
          if features[0] <= 0.007247727255162317:
            return 0
          else:  # if features[0] > 0.007247727255162317
            return 1
      else:  # if features[19] > 0.016111046963487752
        if features[14] <= 0.02333633543457836:
          return 1
        else:  # if features[14] > 0.02333633543457836
          if features[3] <= 0.022427564679674106:
            return 0
          else:  # if features[3] > 0.022427564679674106
            return 1
  else:  # if features[3] > 0.022472442247817526
    if features[7] <= 0.030651379041955806:
      if features[19] <= 0.005374088785174536:
        if features[1] <= 0.032065022438473534:
          if features[5] <= 0.02777921468077693:
            return 0
          else:  # if features[5] > 0.02777921468077693
            return 1
        else:  # if features[1] > 0.032065022438473534
          if features[7] <= 0.012655474216444418:
            return 0
          else:  # if features[7] > 0.012655474216444418
            return 1
      else:  # if features[19] > 0.005374088785174536
        if features[0] <= 0.015415444657264743:
          if features[6] <= 0.025333387216960546:
            return 0
          else:  # if features[6] > 0.025333387216960546
            return 1
        else:  # if features[0] > 0.015415444657264743
          if features[14] <= 0.006899926102050813:
            return 1
          else:  # if features[14] > 0.006899926102050813
            return 0
    else:  # if features[7] > 0.030651379041955806
      if features[19] <= 0.0327718441367324:
        if features[0] <= 0.09189804016568814:
          if features[3] <= 0.027061173590482213:
            return 1
          else:  # if features[3] > 0.027061173590482213
            return 1
        else:  # if features[0] > 0.09189804016568814
          return 0
      else:  # if features[19] > 0.0327718441367324
        if features[19] <= 0.04110785241937265:
          if features[17] <= 0.053404306090669706:
            return 0
          else:  # if features[17] > 0.053404306090669706
            return 1
        else:  # if features[19] > 0.04110785241937265
          if features[19] <= 0.04468683847881039:
            return 0
          else:  # if features[19] > 0.04468683847881039
            return 0
##################################################
def tree_13b(features):
  if features[3] <= 0.02248366163985338:
    if features[7] <= 0.030786011746386066:
      if features[0] <= 0.03417426814121427:
        if features[11] <= 0.007651625368453097:
          if features[0] <= 0.03390500273235375:
            return 0
          else:  # if features[0] > 0.03390500273235375
            return 0
        else:  # if features[11] > 0.007651625368453097
          if features[1] <= 0.02820555157813942:
            return 0
          else:  # if features[1] > 0.02820555157813942
            return 0
      else:  # if features[0] > 0.03417426814121427
        if features[7] <= 0.009760871071193833:
          if features[15] <= 0.0021316844868124463:
            return 0
          else:  # if features[15] > 0.0021316844868124463
            return 0
        else:  # if features[7] > 0.009760871071193833
          if features[17] <= 0.005295553040923551:
            return 1
          else:  # if features[17] > 0.005295553040923551
            return 0
    else:  # if features[7] > 0.030786011746386066
      if features[19] <= 0.016111046963487752:
        if features[10] <= 0.019252476733527146:
          if features[5] <= 0.031975267302186694:
            return 0
          else:  # if features[5] > 0.031975267302186694
            return 1
        else:  # if features[10] > 0.019252476733527146
          if features[0] <= 0.007247727255162317:
            return 0
          else:  # if features[0] > 0.007247727255162317
            return 1
      else:  # if features[19] > 0.016111046963487752
        if features[14] <= 0.02333633543457836:
          return 1
        else:  # if features[14] > 0.02333633543457836
          if features[3] <= 0.02241634528763825:
            return 0
          else:  # if features[3] > 0.02241634528763825
            return 1
  else:  # if features[3] > 0.02248366163985338
    if features[7] <= 0.030651379041955806:
      if features[19] <= 0.005362869393138681:
        if features[1] <= 0.032065022438473534:
          if features[5] <= 0.02777921468077693:
            return 0
          else:  # if features[5] > 0.02777921468077693
            return 1
        else:  # if features[1] > 0.032065022438473534
          if features[7] <= 0.012655474216444418:
            return 0
          else:  # if features[7] > 0.012655474216444418
            return 1
      else:  # if features[19] > 0.005362869393138681
        if features[0] <= 0.015415444657264743:
          if features[6] <= 0.025333387216960546:
            return 0
          else:  # if features[6] > 0.025333387216960546
            return 1
        else:  # if features[0] > 0.015415444657264743
          if features[14] <= 0.006888706710014958:
            return 1
          else:  # if features[14] > 0.006888706710014958
            return 0
    else:  # if features[7] > 0.030651379041955806
      if features[19] <= 0.03278306352876825:
        if features[0] <= 0.09188682077365229:
          if features[3] <= 0.027061173590482213:
            return 1
          else:  # if features[3] > 0.027061173590482213
            return 1
        else:  # if features[0] > 0.09188682077365229
          return 0
      else:  # if features[19] > 0.03278306352876825
        if features[19] <= 0.04110785241937265:
          if features[17] <= 0.053404306090669706:
            return 0
          else:  # if features[17] > 0.053404306090669706
            return 1
        else:  # if features[19] > 0.04110785241937265
          if features[19] <= 0.04469805787084624:
            return 0
          else:  # if features[19] > 0.04469805787084624
            return 0
##################################################
def tree_12b(features):
  if features[3] <= 0.02248366163985338:
    if features[7] <= 0.030786011746386066:
      if features[0] <= 0.03415182935714256:
        if features[11] <= 0.007629186584381387:
          if features[0] <= 0.03392744151642546:
            return 0
          else:  # if features[0] > 0.03392744151642546
            return 0
        else:  # if features[11] > 0.007629186584381387
          if features[1] <= 0.02822799036221113:
            return 0
          else:  # if features[1] > 0.02822799036221113
            return 0
      else:  # if features[0] > 0.03415182935714256
        if features[7] <= 0.009783309855265543:
          if features[15] <= 0.0021092457027407363:
            return 0
          else:  # if features[15] > 0.0021092457027407363
            return 0
        else:  # if features[7] > 0.009783309855265543
          if features[17] <= 0.005295553040923551:
            return 1
          else:  # if features[17] > 0.005295553040923551
            return 0
    else:  # if features[7] > 0.030786011746386066
      if features[19] <= 0.016111046963487752:
        if features[10] <= 0.019252476733527146:
          if features[5] <= 0.031997706086258404:
            return 0
          else:  # if features[5] > 0.031997706086258404
            return 1
        else:  # if features[10] > 0.019252476733527146
          if features[0] <= 0.007225288471090607:
            return 0
          else:  # if features[0] > 0.007225288471090607
            return 1
      else:  # if features[19] > 0.016111046963487752
        if features[14] <= 0.02333633543457836:
          return 1
        else:  # if features[14] > 0.02333633543457836
          if features[3] <= 0.02243878407170996:
            return 0
          else:  # if features[3] > 0.02243878407170996
            return 1
  else:  # if features[3] > 0.02248366163985338
    if features[7] <= 0.030651379041955806:
      if features[19] <= 0.005385308177210391:
        if features[1] <= 0.032042583654401824:
          if features[5] <= 0.02777921468077693:
            return 0
          else:  # if features[5] > 0.02777921468077693
            return 1
        else:  # if features[1] > 0.032042583654401824
          if features[7] <= 0.012655474216444418:
            return 0
          else:  # if features[7] > 0.012655474216444418
            return 1
      else:  # if features[19] > 0.005385308177210391
        if features[0] <= 0.015437883441336453:
          if features[6] <= 0.025355826001032256:
            return 0
          else:  # if features[6] > 0.025355826001032256
            return 1
        else:  # if features[0] > 0.015437883441336453
          if features[14] <= 0.006911145494086668:
            return 1
          else:  # if features[14] > 0.006911145494086668
            return 0
    else:  # if features[7] > 0.030651379041955806
      if features[19] <= 0.03276062474469654:
        if features[0] <= 0.09186438198958058:
          if features[3] <= 0.027061173590482213:
            return 1
          else:  # if features[3] > 0.027061173590482213
            return 1
        else:  # if features[0] > 0.09186438198958058
          return 0
      else:  # if features[19] > 0.03276062474469654
        if features[19] <= 0.04110785241937265:
          if features[17] <= 0.053404306090669706:
            return 0
          else:  # if features[17] > 0.053404306090669706
            return 1
        else:  # if features[19] > 0.04110785241937265
          if features[19] <= 0.04469805787084624:
            return 0
          else:  # if features[19] > 0.04469805787084624
            return 0
##################################################
def tree_11b(features):
  if features[3] <= 0.02243878407170996:
    if features[7] <= 0.030786011746386066:
      if features[0] <= 0.03419670692528598:
        if features[11] <= 0.007629186584381387:
          if features[0] <= 0.03392744151642546:
            return 0
          else:  # if features[0] > 0.03392744151642546
            return 0
        else:  # if features[11] > 0.007629186584381387
          if features[1] <= 0.02818311279406771:
            return 0
          else:  # if features[1] > 0.02818311279406771
            return 0
      else:  # if features[0] > 0.03419670692528598
        if features[7] <= 0.009783309855265543:
          if features[15] <= 0.0021541232708841562:
            return 0
          else:  # if features[15] > 0.0021541232708841562
            return 0
        else:  # if features[7] > 0.009783309855265543
          if features[17] <= 0.005295553040923551:
            return 1
          else:  # if features[17] > 0.005295553040923551
            return 0
    else:  # if features[7] > 0.030786011746386066
      if features[19] <= 0.01615592453163117:
        if features[10] <= 0.019297354301670566:
          if features[5] <= 0.031952828518114984:
            return 0
          else:  # if features[5] > 0.031952828518114984
            return 1
        else:  # if features[10] > 0.019297354301670566
          if features[0] <= 0.007270166039234027:
            return 0
          else:  # if features[0] > 0.007270166039234027
            return 1
      else:  # if features[19] > 0.01615592453163117
        if features[14] <= 0.02333633543457836:
          return 1
        else:  # if features[14] > 0.02333633543457836
          if features[3] <= 0.02243878407170996:
            return 0
          else:  # if features[3] > 0.02243878407170996
            return 1
  else:  # if features[3] > 0.02243878407170996
    if features[7] <= 0.030696256610099226:
      if features[19] <= 0.005385308177210391:
        if features[1] <= 0.032042583654401824:
          if features[5] <= 0.02773433711263351:
            return 0
          else:  # if features[5] > 0.02773433711263351
            return 1
        else:  # if features[1] > 0.032042583654401824
          if features[7] <= 0.012655474216444418:
            return 0
          else:  # if features[7] > 0.012655474216444418
            return 1
      else:  # if features[19] > 0.005385308177210391
        if features[0] <= 0.015437883441336453:
          if features[6] <= 0.025310948432888836:
            return 0
          else:  # if features[6] > 0.025310948432888836
            return 1
        else:  # if features[0] > 0.015437883441336453
          if features[14] <= 0.006911145494086668:
            return 1
          else:  # if features[14] > 0.006911145494086668
            return 0
    else:  # if features[7] > 0.030696256610099226
      if features[19] <= 0.03276062474469654:
        if features[0] <= 0.09181950442143716:
          if features[3] <= 0.027106051158625633:
            return 1
          else:  # if features[3] > 0.027106051158625633
            return 1
        else:  # if features[0] > 0.09181950442143716
          return 0
      else:  # if features[19] > 0.03276062474469654
        if features[19] <= 0.04110785241937265:
          if features[17] <= 0.053404306090669706:
            return 0
          else:  # if features[17] > 0.053404306090669706
            return 1
        else:  # if features[19] > 0.04110785241937265
          if features[19] <= 0.04469805787084624:
            return 0
          else:  # if features[19] > 0.04469805787084624
            return 0
##################################################
def tree_10b(features):
  if features[3] <= 0.02243878407170996:
    if features[7] <= 0.030696256610099226:
      if features[0] <= 0.03410695178899914:
        if features[11] <= 0.0077189417206682265:
          if features[0] <= 0.03392744151642546:
            return 0
          else:  # if features[0] > 0.03392744151642546
            return 0
        else:  # if features[11] > 0.0077189417206682265
          if features[1] <= 0.02818311279406771:
            return 0
          else:  # if features[1] > 0.02818311279406771
            return 0
      else:  # if features[0] > 0.03410695178899914
        if features[7] <= 0.009693554718978703:
          if features[15] <= 0.0021541232708841562:
            return 0
          else:  # if features[15] > 0.0021541232708841562
            return 0
        else:  # if features[7] > 0.009693554718978703
          if features[17] <= 0.005205797904636711:
            return 1
          else:  # if features[17] > 0.005205797904636711
            return 0
    else:  # if features[7] > 0.030696256610099226
      if features[19] <= 0.01615592453163117:
        if features[10] <= 0.019207599165383726:
          if features[5] <= 0.031952828518114984:
            return 0
          else:  # if features[5] > 0.031952828518114984
            return 1
        else:  # if features[10] > 0.019207599165383726
          if features[0] <= 0.007180410902947187:
            return 0
          else:  # if features[0] > 0.007180410902947187
            return 1
      else:  # if features[19] > 0.01615592453163117
        if features[14] <= 0.02333633543457836:
          return 1
        else:  # if features[14] > 0.02333633543457836
          if features[3] <= 0.02243878407170996:
            return 0
          else:  # if features[3] > 0.02243878407170996
            return 1
  else:  # if features[3] > 0.02243878407170996
    if features[7] <= 0.030696256610099226:
      if features[19] <= 0.005385308177210391:
        if features[1] <= 0.032132338790688664:
          if features[5] <= 0.02782409224892035:
            return 0
          else:  # if features[5] > 0.02782409224892035
            return 1
        else:  # if features[1] > 0.032132338790688664
          if features[7] <= 0.012745229352731258:
            return 0
          else:  # if features[7] > 0.012745229352731258
            return 1
      else:  # if features[19] > 0.005385308177210391
        if features[0] <= 0.015437883441336453:
          if features[6] <= 0.025310948432888836:
            return 0
          else:  # if features[6] > 0.025310948432888836
            return 1
        else:  # if features[0] > 0.015437883441336453
          if features[14] <= 0.006821390357799828:
            return 1
          else:  # if features[14] > 0.006821390357799828
            return 0
    else:  # if features[7] > 0.030696256610099226
      if features[19] <= 0.03285037988098338:
        if features[0] <= 0.09172974928515032:
          if features[3] <= 0.027106051158625633:
            return 1
          else:  # if features[3] > 0.027106051158625633
            return 1
        else:  # if features[0] > 0.09172974928515032
          return 0
      else:  # if features[19] > 0.03285037988098338
        if features[19] <= 0.04110785241937265:
          if features[17] <= 0.053494061226956546:
            return 0
          else:  # if features[17] > 0.053494061226956546
            return 1
        else:  # if features[19] > 0.04110785241937265
          if features[19] <= 0.04469805787084624:
            return 0
          else:  # if features[19] > 0.04469805787084624
            return 0
##################################################
def tree_9b(features):
  if features[3] <= 0.02261829434428364:
    if features[7] <= 0.030875766882672906:
      if features[0] <= 0.03410695178899914:
        if features[11] <= 0.007539431448094547:
          if features[0] <= 0.03374793124385178:
            return 0
          else:  # if features[0] > 0.03374793124385178
            return 0
        else:  # if features[11] > 0.007539431448094547
          if features[1] <= 0.02836262306664139:
            return 0
          else:  # if features[1] > 0.02836262306664139
            return 0
      else:  # if features[0] > 0.03410695178899914
        if features[7] <= 0.009693554718978703:
          if features[15] <= 0.0021541232708841562:
            return 0
          else:  # if features[15] > 0.0021541232708841562
            return 0
        else:  # if features[7] > 0.009693554718978703
          if features[17] <= 0.005385308177210391:
            return 1
          else:  # if features[17] > 0.005385308177210391
            return 0
    else:  # if features[7] > 0.030875766882672906
      if features[19] <= 0.01615592453163117:
        if features[10] <= 0.019387109437957406:
          if features[5] <= 0.031952828518114984:
            return 0
          else:  # if features[5] > 0.031952828518114984
            return 1
        else:  # if features[10] > 0.019387109437957406
          if features[0] <= 0.007180410902947187:
            return 0
          else:  # if features[0] > 0.007180410902947187
            return 1
      else:  # if features[19] > 0.01615592453163117
        if features[14] <= 0.02333633543457836:
          return 1
        else:  # if features[14] > 0.02333633543457836
          if features[3] <= 0.02225927379913628:
            return 0
          else:  # if features[3] > 0.02225927379913628
            return 1
  else:  # if features[3] > 0.02261829434428364
    if features[7] <= 0.030516746337525547:
      if features[19] <= 0.005385308177210391:
        if features[1] <= 0.031952828518114984:
          if features[5] <= 0.02764458197634667:
            return 0
          else:  # if features[5] > 0.02764458197634667
            return 1
        else:  # if features[1] > 0.031952828518114984
          if features[7] <= 0.012565719080157578:
            return 0
          else:  # if features[7] > 0.012565719080157578
            return 1
      else:  # if features[19] > 0.005385308177210391
        if features[0] <= 0.015437883441336453:
          if features[6] <= 0.025490458705462515:
            return 0
          else:  # if features[6] > 0.025490458705462515
            return 1
        else:  # if features[0] > 0.015437883441336453
          if features[14] <= 0.006821390357799828:
            return 1
          else:  # if features[14] > 0.006821390357799828
            return 0
    else:  # if features[7] > 0.030516746337525547
      if features[19] <= 0.0326708696084097:
        if features[0] <= 0.09155023901257664:
          if features[3] <= 0.026926540886051953:
            return 1
          else:  # if features[3] > 0.026926540886051953
            return 1
        else:  # if features[0] > 0.09155023901257664
          return 0
      else:  # if features[19] > 0.0326708696084097
        if features[19] <= 0.04092834214679897:
          if features[17] <= 0.053494061226956546:
            return 0
          else:  # if features[17] > 0.053494061226956546
            return 1
        else:  # if features[19] > 0.04092834214679897
          if features[19] <= 0.04451854759827256:
            return 0
          else:  # if features[19] > 0.04451854759827256
            return 0
##################################################
def tree_8b(features):
  if features[3] <= 0.02225927379913628:
    if features[7] <= 0.030875766882672906:
      if features[0] <= 0.0344659723341465:
        if features[11] <= 0.007898451993241906:
          if features[0] <= 0.03374793124385178:
            return 0
          else:  # if features[0] > 0.03374793124385178
            return 0
        else:  # if features[11] > 0.007898451993241906
          if features[1] <= 0.02800360252149403:
            return 0
          else:  # if features[1] > 0.02800360252149403
            return 0
      else:  # if features[0] > 0.0344659723341465
        if features[7] <= 0.010052575264126062:
          if features[15] <= 0.0021541232708841562:
            return 0
          else:  # if features[15] > 0.0021541232708841562
            return 0
        else:  # if features[7] > 0.010052575264126062
          if features[17] <= 0.005026287632063031:
            return 1
          else:  # if features[17] > 0.005026287632063031
            return 0
    else:  # if features[7] > 0.030875766882672906
      if features[19] <= 0.015796903986483812:
        if features[10] <= 0.019387109437957406:
          if features[5] <= 0.03231184906326234:
            return 0
          else:  # if features[5] > 0.03231184906326234
            return 1
        else:  # if features[10] > 0.019387109437957406
          if features[0] <= 0.007180410902947187:
            return 0
          else:  # if features[0] > 0.007180410902947187
            return 1
      else:  # if features[19] > 0.015796903986483812
        if features[14] <= 0.022977314889431:
          return 1
        else:  # if features[14] > 0.022977314889431
          if features[3] <= 0.02225927379913628:
            return 0
          else:  # if features[3] > 0.02225927379913628
            return 1
  else:  # if features[3] > 0.02225927379913628
    if features[7] <= 0.030875766882672906:
      if features[19] <= 0.005026287632063031:
        if features[1] <= 0.03231184906326234:
          if features[5] <= 0.02800360252149403:
            return 0
          else:  # if features[5] > 0.02800360252149403
            return 1
        else:  # if features[1] > 0.03231184906326234
          if features[7] <= 0.012924739625304937:
            return 0
          else:  # if features[7] > 0.012924739625304937
            return 1
      else:  # if features[19] > 0.005026287632063031
        if features[0] <= 0.015078862896189094:
          if features[6] <= 0.025131438160315156:
            return 0
          else:  # if features[6] > 0.025131438160315156
            return 1
        else:  # if features[0] > 0.015078862896189094
          if features[14] <= 0.007180410902947187:
            return 1
          else:  # if features[14] > 0.007180410902947187
            return 0
    else:  # if features[7] > 0.030875766882672906
      if features[19] <= 0.03302989015355706:
        if features[0] <= 0.09119121846742928:
          if features[3] <= 0.027285561431199312:
            return 1
          else:  # if features[3] > 0.027285561431199312
            return 1
        else:  # if features[0] > 0.09119121846742928
          return 0
      else:  # if features[19] > 0.03302989015355706
        if features[19] <= 0.04092834214679897:
          if features[17] <= 0.05313504068180919:
            return 0
          else:  # if features[17] > 0.05313504068180919
            return 1
        else:  # if features[19] > 0.04092834214679897
          if features[19] <= 0.04451854759827256:
            return 0
          else:  # if features[19] > 0.04451854759827256
            return 0
##################################################
def tree_7b(features):
  if features[3] <= 0.022977314889431:
    if features[7] <= 0.030157725792378187:
      if features[0] <= 0.0344659723341465:
        if features[11] <= 0.007180410902947187:
          if features[0] <= 0.0344659723341465:
            return 0
          else:  # if features[0] > 0.0344659723341465
            return 0
        else:  # if features[11] > 0.007180410902947187
          if features[1] <= 0.02872164361178875:
            return 0
          else:  # if features[1] > 0.02872164361178875
            return 0
      else:  # if features[0] > 0.0344659723341465
        if features[7] <= 0.010052575264126062:
          if features[15] <= 0.0014360821805894375:
            return 0
          else:  # if features[15] > 0.0014360821805894375
            return 0
        else:  # if features[7] > 0.010052575264126062
          if features[17] <= 0.00574432872235775:
            return 1
          else:  # if features[17] > 0.00574432872235775
            return 0
    else:  # if features[7] > 0.030157725792378187
      if features[19] <= 0.015796903986483812:
        if features[10] <= 0.018669068347662687:
          if features[5] <= 0.031593807972967625:
            return 0
          else:  # if features[5] > 0.031593807972967625
            return 1
        else:  # if features[10] > 0.018669068347662687
          if features[0] <= 0.007180410902947187:
            return 0
          else:  # if features[0] > 0.007180410902947187
            return 1
      else:  # if features[19] > 0.015796903986483812
        if features[14] <= 0.022977314889431:
          return 1
        else:  # if features[14] > 0.022977314889431
          if features[3] <= 0.022977314889431:
            return 0
          else:  # if features[3] > 0.022977314889431
            return 1
  else:  # if features[3] > 0.022977314889431
    if features[7] <= 0.030157725792378187:
      if features[19] <= 0.00574432872235775:
        if features[1] <= 0.031593807972967625:
          if features[5] <= 0.027285561431199312:
            return 0
          else:  # if features[5] > 0.027285561431199312
            return 1
        else:  # if features[1] > 0.031593807972967625
          if features[7] <= 0.012924739625304937:
            return 0
          else:  # if features[7] > 0.012924739625304937
            return 1
      else:  # if features[19] > 0.00574432872235775
        if features[0] <= 0.015796903986483812:
          if features[6] <= 0.025849479250609875:
            return 0
          else:  # if features[6] > 0.025849479250609875
            return 1
        else:  # if features[0] > 0.015796903986483812
          if features[14] <= 0.007180410902947187:
            return 1
          else:  # if features[14] > 0.007180410902947187
            return 0
    else:  # if features[7] > 0.030157725792378187
      if features[19] <= 0.03302989015355706:
        if features[0] <= 0.09047317737713456:
          if features[3] <= 0.027285561431199312:
            return 1
          else:  # if features[3] > 0.027285561431199312
            return 1
        else:  # if features[0] > 0.09047317737713456
          return 0
      else:  # if features[19] > 0.03302989015355706
        if features[19] <= 0.04164638323709369:
          if features[17] <= 0.05313504068180919:
            return 0
          else:  # if features[17] > 0.05313504068180919
            return 1
        else:  # if features[19] > 0.04164638323709369
          if features[19] <= 0.04451854759827256:
            return 0
          else:  # if features[19] > 0.04451854759827256
            return 0
##################################################
def tree_6b(features):
  if features[3] <= 0.022977314889431:
    if features[7] <= 0.031593807972967625:
      if features[0] <= 0.0344659723341465:
        if features[11] <= 0.008616493083536625:
          if features[0] <= 0.0344659723341465:
            return 0
          else:  # if features[0] > 0.0344659723341465
            return 0
        else:  # if features[11] > 0.008616493083536625
          if features[1] <= 0.02872164361178875:
            return 0
          else:  # if features[1] > 0.02872164361178875
            return 0
      else:  # if features[0] > 0.0344659723341465
        if features[7] <= 0.008616493083536625:
          if features[15] <= 0.002872164361178875:
            return 0
          else:  # if features[15] > 0.002872164361178875
            return 0
        else:  # if features[7] > 0.008616493083536625
          if features[17] <= 0.00574432872235775:
            return 1
          else:  # if features[17] > 0.00574432872235775
            return 0
    else:  # if features[7] > 0.031593807972967625
      if features[19] <= 0.01723298616707325:
        if features[10] <= 0.020105150528252125:
          if features[5] <= 0.031593807972967625:
            return 0
          else:  # if features[5] > 0.031593807972967625
            return 1
        else:  # if features[10] > 0.020105150528252125
          if features[0] <= 0.008616493083536625:
            return 0
          else:  # if features[0] > 0.008616493083536625
            return 1
      else:  # if features[19] > 0.01723298616707325
        if features[14] <= 0.022977314889431:
          return 1
        else:  # if features[14] > 0.022977314889431
          if features[3] <= 0.022977314889431:
            return 0
          else:  # if features[3] > 0.022977314889431
            return 1
  else:  # if features[3] > 0.022977314889431
    if features[7] <= 0.031593807972967625:
      if features[19] <= 0.00574432872235775:
        if features[1] <= 0.031593807972967625:
          if features[5] <= 0.02872164361178875:
            return 0
          else:  # if features[5] > 0.02872164361178875
            return 1
        else:  # if features[1] > 0.031593807972967625
          if features[7] <= 0.0114886574447155:
            return 0
          else:  # if features[7] > 0.0114886574447155
            return 1
      else:  # if features[19] > 0.00574432872235775
        if features[0] <= 0.014360821805894375:
          if features[6] <= 0.025849479250609875:
            return 0
          else:  # if features[6] > 0.025849479250609875
            return 1
        else:  # if features[0] > 0.014360821805894375
          if features[14] <= 0.00574432872235775:
            return 1
          else:  # if features[14] > 0.00574432872235775
            return 0
    else:  # if features[7] > 0.031593807972967625
      if features[19] <= 0.031593807972967625:
        if features[0] <= 0.08903709519654512:
          if features[3] <= 0.025849479250609875:
            return 1
          else:  # if features[3] > 0.025849479250609875
            return 1
        else:  # if features[0] > 0.08903709519654512
          return 0
      else:  # if features[19] > 0.031593807972967625
        if features[19] <= 0.04021030105650425:
          if features[17] <= 0.054571122862398624:
            return 0
          else:  # if features[17] > 0.054571122862398624
            return 1
        else:  # if features[19] > 0.04021030105650425
          if features[19] <= 0.045954629778862:
            return 0
          else:  # if features[19] > 0.045954629778862
            return 0
##################################################
def tree_5b(features):
  if features[3] <= 0.022977314889431:
    if features[7] <= 0.02872164361178875:
      if features[0] <= 0.0344659723341465:
        if features[11] <= 0.00574432872235775:
          if features[0] <= 0.0344659723341465:
            return 0
          else:  # if features[0] > 0.0344659723341465
            return 0
        else:  # if features[11] > 0.00574432872235775
          if features[1] <= 0.02872164361178875:
            return 0
          else:  # if features[1] > 0.02872164361178875
            return 0
      else:  # if features[0] > 0.0344659723341465
        if features[7] <= 0.0114886574447155:
          if features[15] <= 0.0:
            return 0
          else:  # if features[15] > 0.0
            return 0
        else:  # if features[7] > 0.0114886574447155
          if features[17] <= 0.00574432872235775:
            return 1
          else:  # if features[17] > 0.00574432872235775
            return 0
    else:  # if features[7] > 0.02872164361178875
      if features[19] <= 0.01723298616707325:
        if features[10] <= 0.01723298616707325:
          if features[5] <= 0.0344659723341465:
            return 0
          else:  # if features[5] > 0.0344659723341465
            return 1
        else:  # if features[10] > 0.01723298616707325
          if features[0] <= 0.00574432872235775:
            return 0
          else:  # if features[0] > 0.00574432872235775
            return 1
      else:  # if features[19] > 0.01723298616707325
        if features[14] <= 0.022977314889431:
          return 1
        else:  # if features[14] > 0.022977314889431
          if features[3] <= 0.022977314889431:
            return 0
          else:  # if features[3] > 0.022977314889431
            return 1
  else:  # if features[3] > 0.022977314889431
    if features[7] <= 0.02872164361178875:
      if features[19] <= 0.00574432872235775:
        if features[1] <= 0.0344659723341465:
          if features[5] <= 0.02872164361178875:
            return 0
          else:  # if features[5] > 0.02872164361178875
            return 1
        else:  # if features[1] > 0.0344659723341465
          if features[7] <= 0.0114886574447155:
            return 0
          else:  # if features[7] > 0.0114886574447155
            return 1
      else:  # if features[19] > 0.00574432872235775
        if features[0] <= 0.01723298616707325:
          if features[6] <= 0.022977314889431:
            return 0
          else:  # if features[6] > 0.022977314889431
            return 1
        else:  # if features[0] > 0.01723298616707325
          if features[14] <= 0.00574432872235775:
            return 1
          else:  # if features[14] > 0.00574432872235775
            return 0
    else:  # if features[7] > 0.02872164361178875
      if features[19] <= 0.0344659723341465:
        if features[0] <= 0.08616493083536625:
          if features[3] <= 0.02872164361178875:
            return 1
          else:  # if features[3] > 0.02872164361178875
            return 1
        else:  # if features[0] > 0.08616493083536625
          return 0
      else:  # if features[19] > 0.0344659723341465
        if features[19] <= 0.04021030105650425:
          if features[17] <= 0.05169895850121975:
            return 0
          else:  # if features[17] > 0.05169895850121975
            return 1
        else:  # if features[19] > 0.04021030105650425
          if features[19] <= 0.045954629778862:
            return 0
          else:  # if features[19] > 0.045954629778862
            return 0
##################################################
def tree_4b(features):
  if features[3] <= 0.022977314889431:
    if features[7] <= 0.0344659723341465:
      if features[0] <= 0.0344659723341465:
        if features[11] <= 0.0114886574447155:
          if features[0] <= 0.0344659723341465:
            return 0
          else:  # if features[0] > 0.0344659723341465
            return 0
        else:  # if features[11] > 0.0114886574447155
          if features[1] <= 0.022977314889431:
            return 0
          else:  # if features[1] > 0.022977314889431
            return 0
      else:  # if features[0] > 0.0344659723341465
        if features[7] <= 0.0114886574447155:
          if features[15] <= 0.0:
            return 0
          else:  # if features[15] > 0.0
            return 0
        else:  # if features[7] > 0.0114886574447155
          if features[17] <= 0.0:
            return 1
          else:  # if features[17] > 0.0
            return 0
    else:  # if features[7] > 0.0344659723341465
      if features[19] <= 0.0114886574447155:
        if features[10] <= 0.022977314889431:
          if features[5] <= 0.0344659723341465:
            return 0
          else:  # if features[5] > 0.0344659723341465
            return 1
        else:  # if features[10] > 0.022977314889431
          if features[0] <= 0.0114886574447155:
            return 0
          else:  # if features[0] > 0.0114886574447155
            return 1
      else:  # if features[19] > 0.0114886574447155
        if features[14] <= 0.022977314889431:
          return 1
        else:  # if features[14] > 0.022977314889431
          if features[3] <= 0.022977314889431:
            return 0
          else:  # if features[3] > 0.022977314889431
            return 1
  else:  # if features[3] > 0.022977314889431
    if features[7] <= 0.0344659723341465:
      if features[19] <= 0.0:
        if features[1] <= 0.0344659723341465:
          if features[5] <= 0.022977314889431:
            return 0
          else:  # if features[5] > 0.022977314889431
            return 1
        else:  # if features[1] > 0.0344659723341465
          if features[7] <= 0.0114886574447155:
            return 0
          else:  # if features[7] > 0.0114886574447155
            return 1
      else:  # if features[19] > 0.0
        if features[0] <= 0.0114886574447155:
          if features[6] <= 0.022977314889431:
            return 0
          else:  # if features[6] > 0.022977314889431
            return 1
        else:  # if features[0] > 0.0114886574447155
          if features[14] <= 0.0114886574447155:
            return 1
          else:  # if features[14] > 0.0114886574447155
            return 0
    else:  # if features[7] > 0.0344659723341465
      if features[19] <= 0.0344659723341465:
        if features[0] <= 0.0804206021130085:
          if features[3] <= 0.022977314889431:
            return 1
          else:  # if features[3] > 0.022977314889431
            return 1
        else:  # if features[0] > 0.0804206021130085
          return 0
      else:  # if features[19] > 0.0344659723341465
        if features[19] <= 0.045954629778862:
          if features[17] <= 0.0574432872235775:
            return 0
          else:  # if features[17] > 0.0574432872235775
            return 1
        else:  # if features[19] > 0.045954629778862
          if features[19] <= 0.045954629778862:
            return 0
          else:  # if features[19] > 0.045954629778862
            return 0
##################################################
def tree_3b(features):
  if features[3] <= 0.022977314889431:
    if features[7] <= 0.022977314889431:
      if features[0] <= 0.022977314889431:
        if features[11] <= 0.0:
          if features[0] <= 0.022977314889431:
            return 0
          else:  # if features[0] > 0.022977314889431
            return 0
        else:  # if features[11] > 0.0
          if features[1] <= 0.022977314889431:
            return 0
          else:  # if features[1] > 0.022977314889431
            return 0
      else:  # if features[0] > 0.022977314889431
        if features[7] <= 0.0:
          if features[15] <= 0.0:
            return 0
          else:  # if features[15] > 0.0
            return 0
        else:  # if features[7] > 0.0
          if features[17] <= 0.0:
            return 1
          else:  # if features[17] > 0.0
            return 0
    else:  # if features[7] > 0.022977314889431
      if features[19] <= 0.022977314889431:
        if features[10] <= 0.022977314889431:
          if features[5] <= 0.022977314889431:
            return 0
          else:  # if features[5] > 0.022977314889431
            return 1
        else:  # if features[10] > 0.022977314889431
          if features[0] <= 0.0:
            return 0
          else:  # if features[0] > 0.0
            return 1
      else:  # if features[19] > 0.022977314889431
        if features[14] <= 0.022977314889431:
          return 1
        else:  # if features[14] > 0.022977314889431
          if features[3] <= 0.022977314889431:
            return 0
          else:  # if features[3] > 0.022977314889431
            return 1
  else:  # if features[3] > 0.022977314889431
    if features[7] <= 0.022977314889431:
      if features[19] <= 0.0:
        if features[1] <= 0.022977314889431:
          if features[5] <= 0.022977314889431:
            return 0
          else:  # if features[5] > 0.022977314889431
            return 1
        else:  # if features[1] > 0.022977314889431
          if features[7] <= 0.022977314889431:
            return 0
          else:  # if features[7] > 0.022977314889431
            return 1
      else:  # if features[19] > 0.0
        if features[0] <= 0.022977314889431:
          if features[6] <= 0.022977314889431:
            return 0
          else:  # if features[6] > 0.022977314889431
            return 1
        else:  # if features[0] > 0.022977314889431
          if features[14] <= 0.0:
            return 1
          else:  # if features[14] > 0.0
            return 0
    else:  # if features[7] > 0.022977314889431
      if features[19] <= 0.022977314889431:
        if features[0] <= 0.068931944668293:
          if features[3] <= 0.022977314889431:
            return 1
          else:  # if features[3] > 0.022977314889431
            return 1
        else:  # if features[0] > 0.068931944668293
          return 0
      else:  # if features[19] > 0.022977314889431
        if features[19] <= 0.045954629778862:
          if features[17] <= 0.045954629778862:
            return 0
          else:  # if features[17] > 0.045954629778862
            return 1
        else:  # if features[19] > 0.045954629778862
          if features[19] <= 0.045954629778862:
            return 0
          else:  # if features[19] > 0.045954629778862
            return 0
##################################################
def tree_2b(features):
  if features[3] <= 0.0:
    if features[7] <= 0.045954629778862:
      if features[0] <= 0.045954629778862:
        if features[11] <= 0.0:
          if features[0] <= 0.045954629778862:
            return 0
          else:  # if features[0] > 0.045954629778862
            return 0
        else:  # if features[11] > 0.0
          if features[1] <= 0.045954629778862:
            return 0
          else:  # if features[1] > 0.045954629778862
            return 0
      else:  # if features[0] > 0.045954629778862
        if features[7] <= 0.0:
          if features[15] <= 0.0:
            return 0
          else:  # if features[15] > 0.0
            return 0
        else:  # if features[7] > 0.0
          if features[17] <= 0.0:
            return 1
          else:  # if features[17] > 0.0
            return 0
    else:  # if features[7] > 0.045954629778862
      if features[19] <= 0.0:
        if features[10] <= 0.0:
          if features[5] <= 0.045954629778862:
            return 0
          else:  # if features[5] > 0.045954629778862
            return 1
        else:  # if features[10] > 0.0
          if features[0] <= 0.0:
            return 0
          else:  # if features[0] > 0.0
            return 1
      else:  # if features[19] > 0.0
        if features[14] <= 0.045954629778862:
          return 1
        else:  # if features[14] > 0.045954629778862
          if features[3] <= 0.0:
            return 0
          else:  # if features[3] > 0.0
            return 1
  else:  # if features[3] > 0.0
    if features[7] <= 0.045954629778862:
      if features[19] <= 0.0:
        if features[1] <= 0.045954629778862:
          if features[5] <= 0.045954629778862:
            return 0
          else:  # if features[5] > 0.045954629778862
            return 1
        else:  # if features[1] > 0.045954629778862
          if features[7] <= 0.0:
            return 0
          else:  # if features[7] > 0.0
            return 1
      else:  # if features[19] > 0.0
        if features[0] <= 0.0:
          if features[6] <= 0.045954629778862:
            return 0
          else:  # if features[6] > 0.045954629778862
            return 1
        else:  # if features[0] > 0.0
          if features[14] <= 0.0:
            return 1
          else:  # if features[14] > 0.0
            return 0
    else:  # if features[7] > 0.045954629778862
      if features[19] <= 0.045954629778862:
        if features[0] <= 0.045954629778862:
          if features[3] <= 0.045954629778862:
            return 1
          else:  # if features[3] > 0.045954629778862
            return 1
        else:  # if features[0] > 0.045954629778862
          return 0
      else:  # if features[19] > 0.045954629778862
        if features[19] <= 0.045954629778862:
          if features[17] <= 0.045954629778862:
            return 0
          else:  # if features[17] > 0.045954629778862
            return 1
        else:  # if features[19] > 0.045954629778862
          if features[19] <= 0.045954629778862:
            return 0
          else:  # if features[19] > 0.045954629778862
            return 0
##################################################
