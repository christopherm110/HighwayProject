hs = open("high_scores", "r")
high_score = hs.readline().strip()
points = 0
high_score_set = False
if high_score != "":
    high_score_set = True
high_score_message = "High score: " + str(high_score)
display_high_score = my_font.render(high_score_message, True, (255, 255, 255))
if not high_score_set:
    hs = open("high_scores", "w")
    hs.write(str(points))
elif high_score_set:
    if points > int(high_score) or not high_score_set:
        hs = open("high_scores", "w")
        hs.write(str(points))
        high_score_message = "High score: " + str(points_p1) + " (NEW HIGH SCORE!)"
display_high_score = my_font.render(high_score_message, True, (255, 255, 255))
