from heapq import heapify, heappush, heappop 
  

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key = lambda x:x[0], reverse=True)
        result = [0] * n
        freeRooms = [i for i in range(n)]
        currentMeetings = []
        
        heapify(freeRooms)
        heapify(currentMeetings)
        
        while meetings:

            while currentMeetings and meetings[-1][0] >= currentMeetings[0][0]:
                chosenRoom = heappop(currentMeetings)[1]
                heappush(freeRooms, chosenRoom)
                    
            if len(freeRooms) > 0:
                chosenRoom = heappop(freeRooms)
                chosenMeeting = meetings.pop()
                heappush(currentMeetings,[chosenMeeting[-1],chosenRoom])
                result[chosenRoom] += 1
            
            else:
                finishedMeeting = heappop(currentMeetings)
                chosenMeeting = meetings.pop()
                newTime = chosenMeeting[1] - chosenMeeting[0] + finishedMeeting[0]
                heappush(currentMeetings,[newTime, finishedMeeting[1]])
                result[finishedMeeting[1]] += 1
                

        return result.index(max(result))