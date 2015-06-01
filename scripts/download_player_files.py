import urllib2

def main():
    for player_id in range(20000):
        try:
            response = urllib2.urlopen('http://worldbaseballhierarchy.com/lgreports/news/html/players/player_%d.html' % player_id)
            html = response.read()
            with open('player_files/player_%d.html' % player_id, 'w') as f:
                print player_id
                f.write(html)
                
        except urllib2.HTTPError:
            pass

if __name__ == '__main__':
    main()