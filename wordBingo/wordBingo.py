import function

line_row = int(input()) 

bingo_card = function.BingoCardCreate(line_row)

pick_word_num = int(input())
for i in range(pick_word_num):
	pick_word = input()
	function.WordCheck(pick_word, bingo_card)

function.LineCheck(line_row, bingo_card)
function.ColumnCheck(line_row, bingo_card)
function.LTop_RBottomCheck(line_row, bingo_card)
function.RTop_LBottomCheck(line_row, bingo_card)

if function.bingo_count > 0:
	print('yes')
else:
	print('no')