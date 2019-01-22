import requests
import pprint


# ***********listCourse开始*************
def listCourse(retType = 0):

	# 默认返回一个Dict
	# 如果retType为1，返回所有课程名称
	# 如果retType为2，返回所有课程id
	# 如果retType为3，返回所有课程信息，是一个list，格式为[{课程信息}]

	payload = {
		'action': 'list_course',
		'pagenum': 1,
		'pagesize': 20
	}

	response = requests.get('http://localhost/api/mgr/sq_mgr/', params = payload)
	retObj = response.json()
	pprint.pprint(retObj)

	if retType == 1:
		return [one['name'] for one in retObj['retlist']]
	elif retType == 2:
		return [one['id'] for one in retObj['retlist']]
	elif retType == 3:
		return retObj['retlist']
	else:
		return retObj
# ***********listCourse结束*************


# ***********deleteCourse开始*************
def deleteCourse(cid):

    payload = {
        'action': 'delete_course',
        'id': cid
    }

    response = requests.delete('http://localhost/api/mgr/sq_mgr/', data = payload)
    response = response.json()
    pprint.pprint(response)
    return response
# ***********deleteCourse结束*************


# ***********deleteAllLessons开始*************
def deleteAllLessons():
    for one in listCourse(2):
        deleteCourse(one)
# ***********deleteAllLessons结束*************


# ***********addCourse开始*************
def addCourse(cname, desc, idx, retType=0):

    # 如果retType为1，返回新增课程的id
    # 默认返回整个消息体的python格式

    payload = {
        'action': 'add_course',
        'data': '''
        {{  "name": "{}", "desc": "{}", "display_idx": "{}"}}
        '''.format(cname, desc, idx)
    }

    response = requests.post('http://localhost/api/mgr/sq_mgr/', data = payload)
    retObj = response.json()
    pprint.pprint(retObj)

    if retType == 1:
        return retObj['id']
    else:
        return retObj
# ***********addCourse结束*************
