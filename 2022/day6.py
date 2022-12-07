from collections import deque
test = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test1 = "nppdvjthqldpwncqszvftbrmjlhg"
test2 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test3 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
test4 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
data = "pwjwljjjvqjqjzqjqvvpgvpggmdgdrrzmzfzmzffzbbjnbjnjddsdpsdsgsgvsgvgmmzvvpspvspsdsbsbffhwhlwwzllftfhhrfrsrrnnngqgtglgfgtffnssrspsqppdvdtdwwpfpzffnpnddvsswjswjjhdjdrjrwwfpwfpfjppzwzvzpzrznzgzcgzgpgfpffwggtbbhsslzztpplltdtqtctrrszrzszpsprptrtgrtrzrvzrvzrrsfsbswsvvbdbjjgljjwqwgqwwtmwwnbbzdbdwwsnntztstbssnjssjmmldmmrrnfrfgfbbszzzlrrwzwtwwbrwrlwrwzwmwqmwwtqwwtvvdqdtqqfnfjnjsnslltcllvmmdmttvsszrsrwssdmdttdmdrmrsrvrllrhlltmlmlzmlzzhvhbbflfsslclpcczmmcjmjccpgprrgnrrzqqmgqggfvgffbsfsbfbttrgtrtptgtjtnnfbfmmrrcmcwwbbmwmvvvtppslsvvlsvswwztwztzqqpggdccmlldlplggrgddlrddvwvsswllsffbllsbbslshslswsllnqlqrqqpmqmtmqtmqtmmbwmbbzdbzbttvptvpvgpvggblbsspgppvmvsswfssfdfrdffpbfpprmrssmbbmggszslzlslblsldsldssjjsrjjjdfdjdtdmdnnncddpfddrjdjvjfvjffftmfmqqqqqfjjhssbzbbfjjmmzgzllphlplhlplfpfnpnsppjjqsshpssjdjzzwvvjfvfnfttmtbbgtgbbdpbbjppzcpzzvcvpvvdcvvcfvvfsvsccmhhrwrjjsrjrvrfvfwvvtftzztlztlthlhrhnnlpnllnmnfmffzpffhlhbhqbhqhfhwwlglnndgdwdswwgtwgtgsttpbprpqpnnbsnbsnszzrszsqzqlqggvhghrrvprvvvqnnmmrwrbrrmttwrrlmrrrddmsddbhdhdjhdhrhffppphghvvtztptjjlppcqcscjscstsmsbspsgpgqgmmndmdvvpnpnrrjtrthhtzzjlzzrwzrrfsfflrrmffhlhglhhhhvwwttlcttbqqzzbzzzbhbsscqqjggqpggqffbttrfrjjjqmmpttlvvqlvqqqtgtrtcrcbcnbbhfbfhbhqbhqbqvbvqvrqvvgttqwqpwqwnnpgngpphjppztptnnrssjqqrplzrvmwmbrbgbnggvzpmphqsrjrdhtslpmmwrhgcndwtbsbrfmsplzqswsnmrwdwwhzmpbqcmjfsmnwqnjmvdczhgmtfjwnjfdllfzdwpwgclpbdqtqnqqqvpthltznfzshhgrwwqclpplmdwtpjszrdwwzfbljcjmqmhptfhvcbvgfjfftbsfglwqldphdzzgcmvtsbhlsdncfjcsqrqrtdhttcwzlbqhvgppbrjfzdzwzprwpfflmdspcmqcbdhsvwjswwbzwnqrshbqfnmtdzrsrjgqngntllcgwjnmjqvtgwvttfqrcjlhbpcrszlngfmdgzprcdttgbjpcdzbhtdghpltcbvcddnslhqthfvzjtspqlzhdprhgtrlqqgtsqwwjqthgdwfgdfzhrnrwlrpqmgqltgldpjqgjzvngrphclbfftnwfnfvsvhftthptqfnvlftdpdhcrjdhfwtpwwvsblgntdwcpnsprhnpjtjsprdrdjwlhnmnzmmjmcdfsctzgmlqwwrwztjndqgpqrvdgplcnntqhfjlzjszpdwnvlwdzzgpzvplglgrmsjgjpmsrdsgzlfblgbgszgdtgsggqvhzmnfcnvlnzrfpqphctlcqccqzslmlsbbztnpncqpgscgdmmsgfwqrzpmbqrmfqsnnggswhmgmtmgdmhwthbgbdsrtnsrvdfdhlhhczgdsdqnpsgjzpbnsmgrvsfdjlhgjfjjwqnrnrbzdzcjlstclpqfnrflgnzbdbzvbjcbgqrrrlfcpgptcghhqqfsvsgljvjhdgdgcjtnrqsctmwhzbmbrfrsvndhfrtwlfgvqcbjsvttrctfshrggdvgbhthnwbwqglrvfbsqnbhdwgzhbccjnlhtcbjlpgrvttthnwvvspnzvqhjvmtwshcstdjhfqhqcgvwqwwwwrfdmnjhldsrhgmtjddsghdmdrpczbcjflmbhszctmvdttfrrqqpwslhvqbjlsrjdjrcqjrhwgjlsqmvdpvvvlbzwtthptpsggddcbqbhrvrpdtncvgndclhpngzgfqdqgwwbrjltjtqbpbtbzjmfmnjnlqmtzvdqdwqhbgptplrgdsfpjzfrpdcdsznwffpnzsmpqjfbcpddqjgfqhqbwsfmzgstfdnzhphhvgbzvjrlmqmrznpctftcmbtdpbfbfpfpjtjhbcrrssnlvtrtnzvwtjwplclpqndpfstjmghmzsllhntprtjwlppjnjgjzlvlcbcwjvrjqjhfnnpmwlpngwtvvbcllmjzqfrwvtvsrvbcpfwcdfwmdwvztwtbrgvlvmfjmpzdzmfbcmrsqfwqjfjfrgmnblnzfzcvgwllvmqfmdlqqgvvjrptlrjcwphvchwhmtwhnlnjprqhlrhmdfptvpshjbzrhptvnqfvjfjcnglnbfhbwghqqjbqzdthjwqzznwfsmqmbsqnwrdrrwjgzjdmgtsqswlqcpshdmcfjttpszqmsjhgfsrvgchgwzbqgbdqhmbndmnmwjsnjjvmtpprbtlwzpvfdnbtjnzzvlwndgbhgwbpllvfghwvwjmlpnzfjzjwwmtvbbfndppbqwhjlwgtswmgffddbhnwqljvgcvfnqmzgvfmjwsbcrpgtcpchlblccgpgpmddsjsfwbnvnsfttnsqjshchdztvsbjwsfmszfwpwsmgzvvcfddtczvvmnhgjffrsfqzfmphpfblmwgcbbrjqzdztzzzjhqmjzrgmwgrqdfqdbjsgwfndqgnmdvjlwdtjpjtpcqlhtcfvnmzjswldrbqjpmrlqwhvnqjshbqqvzwwsdjmspgbvrgvpjjnwsvnvnppvlnqbdllfczjjftpnlrjfvcwgwbdmldtcnczqzcptjjrgglnnbgmrdffgmnnwvjzwbgcncnhzmthswrdsrhchprrrrnhjfnzmsgfjltqzmttvhslnsgcjfgqwcsddfstcstspcpdbznvdrnqhwqsfgqtdbtwspfswfjbzgtqjpvzfhfdblszblmgrmmlwvnwwdsdjjvrsfjfjltcsfccplftvpltqshgnpnqlqcglrhvzldptspnbvjcchnnvzvbbqnnnbnggrhpcgqtgnjdqplswtblgtwqzmltjjhpdttgbcvhfrsdcgjzswvtbbhrpnzmrjhgznbdpqgqdhwcnmgflpdtbzdbvzvslbvvwdpcnwjtvjhgncnljfwlrvqgdrjhdcprsqjrmwwlcrrvsjtlmqmjtcbqwcbmgnvfshdgmmfffzvwjphjfspvdzjsqdlgqfdjwwshdcssqvvgdcvvtmwlfjdvtfllrvltmrsgpdtdqsfjpcvjnqszpnbqqlnpdvhtswbgwnpcqpgzqwlgsmlnlngcdmqhchcdgfmrhfwwrgrrdrhcsbbcrhghdjrcsltchqghvmbvbbpqzqbgwmqrgwchhbvdsqbqrfcbzwjrlqtnmghtjbtjdpngcjzswfmjfphjnftbhdgvwjsvqfbsfgqhfbcrgrsppsvbnpwlhsdrffcmmgzpjfsvllcrbtwrwddthfjvjndzfzbcmglhbzpzwwbtzdpdlwrnbzqjbqwpbdlwfddbtzjhqshmcghqfcrzrmrtmqwpqhvqzbfwhbssgjcmzqcpvnntbpfqwhbmtjdtbtrrdhsvzqjltdshtlvwwmlbdzlvjhmtppnbqcjnncpslcggsjbrmzvdgqzclwszgzfqthndnjfjrznlmmtjwwhnzvhnjncccpczrftvhtdhjbzvwvlgqhdnfqdqrhctfffpcnqzdrgqqzcczdjvpzqfgfcpjzqhbwshsqhvqzpsb"
def processor(x):
    old_arr = [False, False, False]
    pos = 0
    for cur in x:
        pos += 1
        if not old_arr[0]:
            if not old_arr[1]:
                # Always unique 4th oldest character
                if not old_arr[2]:
                    old_arr[2] = cur
                    continue
                # 3rd Oldest, Compare to 4th Oldest
                if cur != old_arr[2]:
                    old_arr[1] = cur
                    continue
                # 3rd and 4th are the same
                continue
            # 2nd Oldest, test if same as 3rd
            if cur == old_arr[1]:
                old_arr[2] = cur
                old_arr[1] = False
                continue
            # 2nd Oldest, test if same as 4th
            if cur == old_arr[2]:
                old_arr[2] = old_arr[1]
                old_arr[1] = cur
                continue
            old_arr[0] = cur
            continue
        if cur == old_arr[0]:
            old_arr[0] = False
            old_arr[1] = False
            old_arr[2] = cur
        elif cur == old_arr[1]:
            old_arr[1] = cur
            old_arr[2] = old_arr[0]
            old_arr[0] = False
        elif cur == old_arr[2]:
            old_arr[0] = cur
            old_arr[1] = old_arr[0]
            old_arr[2] = old_arr[1]
        else:
            print(cur)
            break
    print(pos)

def checkor(arr, x):

    if arr[0]:
        return True, arr
    if len(arr) == 1:
        arr[0] = x
        return False, arr
    wasLetter, arr[1:] = checkor(arr[1:], x)
    if wasLetter:
        arr[0] = x
    return False, arr
def processor(x, mes):
    mes = mes - 1
    old_arr = [False] * mes
    pos = 0
    for cur in x:
        pos += 1
        back_pos = 0
        for term in old_arr:
            if term == cur:
                old_arr[back_pos:] = [False]*len(old_arr[back_pos:])

                de_old_arr = deque(old_arr)
                de_old_arr.rotate(mes-back_pos)
                old_arr = list(de_old_arr)

                break
            back_pos += 1
        """
        if not old_arr[0]:
            if not old_arr[1]:
                if not old_arr[2]:
                    old_arr[2] = cur
                    continue
                old_arr[1] = cur
                continue
            old_arr[0] = cur
            continue
        """
        wasLetter, old_arr = checkor(old_arr, cur)

        if wasLetter:
            print(pos)
            break


processor(test, 4)
processor(test1, 4)
processor(test2, 4)
processor(test3, 4)
processor(test4, 4)
        
processor(data, 4)

processor(test, 14)
processor(test1, 14)
processor(test2, 14)
processor(test3, 14)
processor(test4, 14)
        
processor(data, 14)