#!/bin/bash

array=(%3853705 %65312557 %475606634 %222449113 %392930152 %26636287 %113940 %589052417 %703499 %8742288 %229223539 %609619 %30025183 %215278999 %365481658 %220152180 %852731810 %70014 %749524287 %638162796561465 %235724941 %215298239 %273844 %1034594933 %2204409 %10927 %29595 %85 %237695030250714 %525617824279058 %413607709053742 %205995 %853944709 %1033254291 %1962700 %893604141 %1917506565222380 %1025449435 %2050633565210234 %1015693214 %257474746 %952571698145362 %1015397774 %24687730 %214098779 %142724889 %19002234 %321424183 %430957793 %242334030 %1775568872568816 %241155225 %214098592 %283960 %122059304510716 %902644176460641 %2042093766008957 %591007675 %457634584595027 %13957 %1276 %385370565312557 %176900653014542 %1016979396 %1662338100537626 %2999944 %828548246 %1024021744 %163183 %212978752 %1062955 %4334 %808138302 %808187999 %807410846 %807481946 %1017443799 %808518102 %1023706203 %155642908613734 %1013109260 %237700823 %384367178 %686253721503919 %1033012215 %247433126 %1030965259 %753314133 %264990513 %239679906 %1033652357 %755907325 %642191349321722 %406539870 %2390272567656745)

# download posts for location ids in array
count=0
for id in $array; do
	count=$(( $count + 1 ))
	if [ $(($count%4)) -eq 0 ]; then
	instaloader --login="sunwisdom101@gmail.com" --password="EvOu7CR7Iq2V" --no-videos --geotags --comments --no-compress-json --post-filter="datetime(2020, 2, 1) <= date_utc <= datetime(2020, 4, 5)" --count=2500 --request-timeout=300 $id	
	elif [ $(($count%6)) -eq 0 ]; then	
	instaloader --login="musketeers1128@gmail.com" --password="EvOu7CR7Iq2V" --no-videos --geotags --comments --no-compress-json --post-filter="datetime(2020, 2, 1) <= date_utc <= datetime(2020, 4, 5)" --count=2500 --request-timeout=300 $id	
	elif [ $(($count%3)) -eq 0 ]; then	
	instaloader --login="jadeite.stream@gmail.com" --password="EvOu7CR7Iq2V" --no-videos --geotags --comments --no-compress-json --post-filter="datetime(2020, 2, 1) <= date_utc <= datetime(2020, 4, 5)" --count=2500 --request-timeout=300 $id	
	elif [ $(($count%2)) -eq 0 ]; then	
	instaloader --login="katkit1112@gmail.com" --password="EvOu7CR7Iq2V" --no-videos --geotags --comments --no-compress-json --post-filter="datetime(2020, 2, 1) <= date_utc <= datetime(2020, 4, 5)" --count=2500 --request-timeout=300 $id	
	else
	instaloader --login="cutebarfkitten@gmail.com" --password="EvOu7CR7Iq2V" --no-videos --geotags --comments --no-compress-json --post-filter="datetime(2020, 2, 1) <= date_utc <= datetime(2020, 4, 5)" --count=2500 --request-timeout=300 $id
	fi
done
