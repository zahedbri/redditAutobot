from app.regularbot import randomcomments


def randomcommentbot():
    """
    This will build user rep over time..put it on a cron
    :return:
    """
    x = randomcomments.main()
    x()


randomcommentbot()

