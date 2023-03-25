# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1]) #saglaba otro elemetu numuru ka integer tipa
        if self.type == 'add':
            self.name = query[2] #saglaba treso elementu vardu 

def read_queries():
    n = int(input()) # ievadit cik prasijumus bus jaizpilda
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = [] #glaba visus kontakus, iekavas jo saraksts
    contacts = {} # glaba visus kontaktus kas nav izdzesti, iekavas jo vardnica
    for cur_query in queries:
        if cur_query.type == 'add':
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            if cur_query.number in contacts:
                contacts[cur_query.number].name = cur_query.name # ja ir kontakts ar tādu pašu numuru, tad maina kontakta vardu
            else: # otherwise, just add it
                contacts[cur_query.number]=cur_query
        elif cur_query.type == 'del':
                if cur_query.number in contacts:
                    del contacts[cur_query.number]
        else:
            response = 'not found'
            if cur_query.number in contacts:
                response = contacts[cur_query.number].name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

