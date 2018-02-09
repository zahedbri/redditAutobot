from app.regularbot import upvoteBot, commentbot, randomcomments


def upvote_comment():
    """
    If you want to upvote a specific post
    set number of upvotes
    has timer
    :return:
    """
    x = upvoteBot.main(number=1, submissionid='')
    return x

def writecomment():
    """
    This will write a comment on a specific post
    :return:
    """
    x = commentbot.main(msg='',
                        submissionid='')
    return x

def randomcommentbot():
    """
    This will build user rep over time..put it on a cron
    :return:
    """
    x = randomcomments.main()
    x()


randomcommentbot()



#upvote_comment()
#writecomment()