__NBA Fantasy Team - Optimization Project__

In the 1980s, a New York City sportswriter named Daniel Okrent created fantasy sports with the idea of allowing sports fans to experience a side of sports that they had never experienced. Fantasy sports are internet simulation-based games where players assemble virtual teams of actual professional players. These professional players are ranked by their statistical in-game performance and are then selected by users who place them on their respective teams. These teams then compete against one another based on the performance of those players in actual games. In a standard fantasy league, winning games results in points that a team gets to keep. At the end of the fantasy season, the team with the most points wins the league (aka the championship). In fantasy basketball, a fantasy score is a metric that considers the fundamental statistics (games played, field goal %, three-point%, points per game, rebounds, turnovers, and more) in a basketball game as a number.

For the past couple of years, fantasy basketball has been growing with increasing popularity. This emerging increase has resulted in the demand of fantasy players to find a way to increase their chances of success with their fantasy team. From simulation software, to predictive analytics, many different tools/methods currently exist to aid fantasy users on which players to select onto their teams, each with their own pros and cons. To address this demand, our group attempted to create the ideal tool that fantasy players can use to build their perfect team.

__Objective__

For this project, we are developing an optimization model that takes all 450 current players in the NBA and builds the best fantasy team possible in order to guarantee success in a fantasy basketball league. This model considers each player’s fantasy score, position, salary, team, and more to find whether or not a respective player is the right fit. Additionally, the model also considers which players are best suited to come off the bench as “backup”, when certain players are injured or are not playing.

__Constraints__
* The biggest constraint would be the salary cap. A lot of the best players in the league make quite a bit of money, no team can afford 5 max-contract players.
* Second constraint would be position. We can only have 2 guards, 2 forwards, and 1 center. So at times, we would have to choose one player over the other, which is something our model would have to handle.

We collected our data - in-game statistics, player salary, position, etc. - on all NBA players in the 2019-2020 season from [Hashtag Basketball](https://hashtagbasketball.com/fantasy-basketball-rankings){:target="_blank" rel="noopener"} and [Basketball-Reference](https://www.basketball-reference.com/){:target="_blank" rel="noopener"}. Both websites refresh and update their data logs daily (while the season is ongoing), ensuring data accuracy and reliability.

__Note:__
This project is still in progress and will be updated regularly until the end of April
