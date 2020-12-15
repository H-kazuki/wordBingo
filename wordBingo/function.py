bingo_count = 0 

def BingoCardCreate(line_row):
	bingo_card = [] #ビンゴカード作成のための空のリスト
	for i in range(line_row):
		word = input()
		word_list = word.split()
		bingo_card.append(word_list)
	return bingo_card

#引数Wordlistを介して送られてきたリストの中身全てが"X"のものを数える関数
def BingoJudg(word_list, line_row):
	if word_list.count("X") == line_row:
		global bingo_count
		bingo_count += 1

#選ばれた数字を"X"に置き換える関数
def WordCheck(pick_word, bingo_card):
	i = 0
	for word_list in bingo_card:
		if pick_word in word_list:
			hit_word_index = word_list.index(pick_word)
			bingo_card[i][hit_word_index] = "X"
		i += 1

#行の中でビンゴしているリストを調べる関数
def LineCheck(line_row, bingo_card):
	for word_list in bingo_card:
		BingoJudg(word_list, line_row)

#列の中でビンゴしているリストを調べる関数
def ColumnCheck(line_row, bingo_card):
	for i in range(line_row):
		word_list = [list[i] for list in bingo_card] #ビンゴカードの各行のi番目の数字を取り出しリストにする
		BingoJudg(word_list, line_row)

#左上から右下（＼）のビンゴしているものを調べる関数
def LTop_RBottomCheck(line_row, bingo_card):
	word_list = []
	column_num = 0 #列数を入れるための変数
	for list in bingo_card:
		word_list.append(list[column_num])
		column_num += 1 #列を一つ右へ
	BingoJudg(word_list, line_row)

#右上から左下（／）のビンゴしているものを調べる関数
def RTop_LBottomCheck(line_row, bingo_card):
	word_list = []
	line_row -= 1
	column_num = line_row #列数を入れるための変数
	for list in bingo_card:
		word_list.append(list[column_num])
		column_num -= 1 #列を一つ左へ
	BingoJudg(word_list, line_row)