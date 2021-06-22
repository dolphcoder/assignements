import pySDK

ch = 1

while(ch):
    print('-'*50+'\n'+'*'*21+'POST(1)'+'*'*21+'\n1. Get posts\n2. Get posts based on user\n3. Get post details\n'+'*'*19+'COMMENTS(2)'+'*'*19+'\n1. Get comments\n2. Get comments based on the posts\n'+'\n'+'*'*21+'EXIT(3)'+'*'*21+'\n'+'-'*50)
    n = int(input('Enter Choice: '))
    if n != 3: 
        sn = int(input('Enter Subchoice: '))
        if n == 1:
            if sn == 1:
                pySDK.get_posts()
            elif sn == 2:
                pySDK.get_user_posts(input('Enter userId: '))
            elif sn == 3:
                pySDK.get_posts_details(input('Enter post title: ').lower())
            else:
                print('Invalid Choice!')
        elif n == 2:
            if sn == 1:
                pySDK.get_comments()
            elif sn == 2:
                pySDK.get_post_comments(input('Enter postId: '))
            else:
                print('Invalid Choice!')
        else:
            print('Invalid choice!')
    else:
        ch = 0
