# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class AssignJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'AssignJobs','ccc')

	def get_CallingNumbers(self):
		return self.get_query_params().get('CallingNumbers')

	def set_CallingNumbers(self,CallingNumbers):
		for i in range(len(CallingNumbers)):	
			if CallingNumbers[i] is not None:
				self.add_query_param('CallingNumber.' + str(i + 1) , CallingNumbers[i]);

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_StrategyJson(self):
		return self.get_query_params().get('StrategyJson')

	def set_StrategyJson(self,StrategyJson):
		self.add_query_param('StrategyJson',StrategyJson)

	def get_ScenarioId(self):
		return self.get_query_params().get('ScenarioId')

	def set_ScenarioId(self,ScenarioId):
		self.add_query_param('ScenarioId',ScenarioId)

	def get_JobsJsons(self):
		return self.get_query_params().get('JobsJsons')

	def set_JobsJsons(self,JobsJsons):
		for i in range(len(JobsJsons)):	
			if JobsJsons[i] is not None:
				self.add_query_param('JobsJson.' + str(i + 1) , JobsJsons[i]);