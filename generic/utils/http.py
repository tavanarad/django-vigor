'''
Created on Sep 1, 2014

@author: morteza
'''
import json
import ast


class JsonResponseStruct:
    '''
    We use this class to generalization json responses
    __repr__ function of this class return json string by default so you can pass the class without serialization to HttpResponse.
    
    '''
    def __init__(self):
        self.hasError= True;
        self.errorCode = 500;
        self.message= None;
        self.extraMessage= None;
        self.data = None;
        self.callbackUrl = None;
        
    def __repr__(self):
        return json.dumps(self.__dict__)

def render_post_params(request, *args, **kwargs):
        result = None;
        try:
            if request.method == "POST":
                if request.POST is None or not request.POST:
                    if request.body:
                        result = ast.literal_eval(request.body)
                else:
                    result = request.POST#ast.literal_eval(str(request.POST.dict()))
            elif request.method == "PUT":
                if request.body:
                    result = ast.literal_eval(request.body);
                else:
                    result = request.PUT
            else:
                result = ast.literal_eval(request.body);
        except Exception as ex:
            print ex;
            return None
        return result;
    