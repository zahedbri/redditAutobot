from app import session
from app.regularbot.models import AgorabitWhoMSg

def addthebot(subreddit, username, datestamp):
    imsged = AgorabitWhoMSg(datestamp=datestamp,
                            subreddit=subreddit,
                            username=username,
                            )

    session.add(imsged)
    session.commit()
