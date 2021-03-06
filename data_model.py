# -*- coding: utf-8 -*-
"""
  data_model
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Data Model for CQUPT EPAY project.

  :copyright: (c) 2020/10/26 by wanglei.
  :license: MIT

TODO:
"""

# 大学
class University():
  Name: str # 大学名称必须唯一
  pass

# 院/系/所
class School():
  University: University # 所属大学
  Name: str # 学院名称
  pass

# 班级
class Class():
  School: School # 所属院/系/所
  Name: str # 班号
  StudentNum: int # 班级人数
  pass

# 用户
class User():
  UserName: str # 登录用户名
  Type: str # 取值: 老师 或 学生
  Class: Class # 所属班级
  RealName: str
  StudentOrTeacherID: str # 学号或教工号
  Avatar: str # link to 头像
  pass

# 提前准备用户头像图片 20张 可以重复使用 根据最近未使用进行选择
class UserAvatar():
  Name: str # 头像名称
  Avatar: str # link to 头像图片
  LatestUseTime: datetime.datetime # 上次使用时间

# 竞赛模板
class GameTemplate():

  # 模板基础设置
  Name: str
  Type: str # 单轮对抗，多轮博弈，自由搏击

  # 市场上客户设置
  ClientNum: int # 客户数
  ClientFund: float # 客户初始资金

  # 竞争机构(银行或第三方支付平台)基础设置
  BankNum: int # 银行数量
  BankFund: float # 银行初始资金

  ThirdPartyNum: int # 第三方支付平台数量
  ThirdPartyFund: int # 第三方支付平台初始资金

  # 利率设置
  BankIR: float # 银行存款利率初始值，IR: Interest Rate
  BankIR_UL: float # 银行存款利率上限, UL: Upper Limit
  BankIR_LL: float # 银行存款利率下限，LL：Lower Limit
  BankIR_Step: float # 银行存款利率调整步长，
  """
  说明：
    假设银行的存款利率参数 IR 可以在一个区间内调节：i ∈ [min, max]。
    其中，min 为银行可以调节存款利率的最小值，该值可以取负值 (历史上在
    其他国家存在负利率)；max 为银行可以调节存款利率的最大值，该值必须
    为大于 0 的正值；同时定义一个固定系数 a(调整步长)。即当学生输入存款利率参数
    IR 对存款利率进行调节时，输入的值必须是 a 的倍数。例如 a=0.25%,
    则学生输入的值必须为 0.25% 的倍数 (例如 0.75%，1.5%，5%)。
  """

  ThirdPartyIR: float # 第三方支付平台优惠利率初始值，IR: Interest Rate
  ThirdPartyIR_UL: float # 第三方支付平台优惠利率上限, UL: Upper Limit
  ThirdPartyIR_LL: float # 第三方支付平台优惠利率下限，LL：Lower Limit
  ThirdPartyIR_Step: float # 第三方支付平台优惠利率调整步长，
  """
  说明：
    调整逻辑同银行存款利率
  """

  # 支付费率设置
  BankFR: float # 银行支付费率初始值，FR: Fee Rate
  BankFR_UL: float # 银行支付费率上限, UL: Upper Limit
  BankFR_LL: float # 银行支付费率下限，LL：Lower Limit
  BankFR_Step: float # 银行支付费率调整步长，
  """
  说明：
    假设银行的支付费率参数 FR 可以在一个区间内调节：i ∈ [min, max]。
    其中，min 为银行可以调节支付费率的最小值，该值可以取负值 (历史上在
    其他国家存在负利率)；max 为银行可以调节支付费率的最大值，该值必须
    为大于 0 的正值；同时定义一个固定系数 a(调整步长)。即当学生输入支付费率参数
    FR 对支付费率进行调节时，输入的值必须是 a 的倍数。例如 a=0.25%,
    则学生输入的值必须为 0.25% 的倍数 (例如 0.75%，1.5%，5%)。
  """

  ThirdPartyFR: float # 第三方支付平台支付费率初始值，FR: Fee Rate
  ThirdPartyFR_UL: float # 第三方支付平台支付费率上限, UL: Upper Limit
  ThirdPartyFR_LL: float # 第三方支付平台支付费率下限，LL：Lower Limit
  ThirdPartyFR_Step: float # 第三方支付平台支付费率调整步长，
  """
  说明：
    调整逻辑同银行支付费率
  """

  # 其他设置
  BankLR: float # 银行贷款利率初始值，LR: Loan Rate
  BankLR_UL: float # 银行贷款利率上限, UL: Upper Limit
  BankLR_LL: float # 银行贷款利率下限，LL：Lower Limit
  BankLR_Step: float # 银行贷款利率调整步长，

  BankRR: float # 银行存款准备金率， RR: Reserve Ratio

  IRWeight: float # 利率权重系数

  ClientLoanDislikeDegree: int # 客户对贷款系统厌恶程度, 取值 1 到 10 的整数

  AllowPlayerChgRole: bool # 允许选手修改扮演的角色(银行或第三方支付平台)， 缺省为False

  Avatar: str # link to 代表该模板的头像图片

  pass

# 提前准备竞赛模板头像图片 10张 可以重复使用 根据最近未使用进行选择
class GameTemplateAvatar():
  Name: str # 竞赛模板头像名称
  Avatar: str # link to 竞赛模板头像图片
  LatestUseTime: datetime.datetime # 上次使用时间

# 分组模板
class TeamTemplate():
  Class: Class # 所属班级， 一个班级下又多个分组模板
  Name: str # 分组模式名称
  TeamNum: int # 分组数量
  # 分组详情： 学生姓名， 学号，所在组名称，扮演角色
  Details: list=[
    {
      'StudentName': '', # 学生(竞赛选手)名称
      'StudentNameID': '', # 学生(竞赛选手)学号
      'TeamName': '', # 学生所在团队名称
      'Role': '' # 扮演银行还是第三方支付平台
    }
  ]

  pass

# 单轮竞赛
class SingleRoundGame():
  Name: str # 竞赛名称
  Organizer: User # 竞赛组织者(老师)
  GameTemplate: GameTemplate # 竞赛用的模板
  Class: Class # 参加竞赛的班级
  TeamTemplate: TeamTemplate # 竞赛用的分组模板
  GameStartTime: datetime.datetime # 竞赛开始时间， 老师开启竞赛的时间
  GameEndTime: datetime.datetime # 竞赛结束时间
  # 选手出牌情况
  PlayerCards: list=[
    {
      'StudentName': '', # 学生(竞赛选手)名称
      'StudentNameID': '', # 学生(竞赛选手)学号
      'Role': '', # 银行，还是 第三方支付平台
      'AgencyRepresented': '', # 代表机构的名称
      'AgencyIR': 0.0075, # 设定(出牌)机构利率， 机构包括 银行 和 第三方支付平台
      'AgencyFR': 0.0025, # 设定机构费率
      'AgencyLR': 0.075, # 设定机构贷款利率，第三方支付平台没有这项
      'ShotTime': datetime.datetime, # 出牌时间
    }
  ]
  # 竞赛结果，按选手
  GameResults: list=[
    {
      'StudentName': '', # 学生(竞赛选手)名称
      'StudentNameID': '', # 学生(竞赛选手)学号
      'Role': '', # 银行，还是 第三方支付平台
      'AgencyRepresented': '', # 代表机构的名称
      'ClientNum': 19, # 留存客户数
      'Cash': 1341, # 现金流结余
      'Profit': 34, # 利润
    }
  ]

  pass

# 多轮竞赛
class MultiRoundGame():
  Name: str # 竞赛名称
  Organizer: User # 竞赛组织者(老师)
  GameTemplate: GameTemplate # 竞赛用的模板
  Class: Class # 参加竞赛的班级
  TeamTemplate: TeamTemplate # 竞赛用的分组模板
  GameStartTime: datetime.datetime # 竞赛开始时间， 老师开启竞赛的时间
  GameEndTime: datetime.datetime # 竞赛结束时间
  RoundNum: int # 回合数
  RoundDuration: int # 每回合持续时间
  # 每一轮的情况
  Rounds: list=[
    {
      'RoundID': 1,
      # 选手出牌情况
      'PlayerCards': [
        {
          'StudentName': '', # 学生(竞赛选手)名称
          'StudentNameID': '', # 学生(竞赛选手)学号
          'Role': '', # 银行，还是 第三方支付平台
          'AgencyRepresented': '', # 代表机构的名称
          'AgencyIR': 0.0075, # 设定(出牌)机构利率， 机构包括 银行 和 第三方支付平台
          'AgencyFR': 0.0025, # 设定机构费率
          'AgencyLR': 0.075, # 设定机构贷款利率，第三方支付平台没有这项
          'ShotTime': datetime.datetime, # 出牌时间
        }
      ],
      # 本轮结果，按选手排列
      'GameResults': [
        {
          'StudentName': '', # 学生(竞赛选手)名称
          'StudentNameID': '', # 学生(竞赛选手)学号
          'Role': '', # 银行，还是 第三方支付平台
          'AgencyRepresented': '', # 代表机构的名称
          'ClientNum': 19, # 留存客户数
          'Cash': 1341, # 现金流结余
          'Profit': 34, # 利润
        }
      ]
    }
  ]
  pass

# 自由搏击
class FreeBattleGame():
  Name: str # 竞赛名称
  Organizer: User # 竞赛组织者(老师)
  GameTemplate: GameTemplate # 竞赛用的模板
  Class: Class # 参加竞赛的班级
  TeamTemplate: TeamTemplate # 竞赛用的分组模板
  GameStartTime: datetime.datetime # 竞赛开始时间， 老师开启竞赛的时间
  GameEndTime: datetime.datetime # 竞赛结束时间
  RoundNum: int # 回合数
  RoundDuration: int # 每回合持续时间
  # 选手出牌和结果
  Shots: list=[
    {
      'ShotTime': datetime.datetime, # 出牌时间
      'WhoShot': str, # 出牌选手的学号
      # 选手出牌情况
      'PlayerCards': [
        {
          'StudentName': '', # 学生(竞赛选手)名称
          'StudentNameID': '', # 学生(竞赛选手)学号
          'Role': '', # 银行，还是 第三方支付平台
          'AgencyRepresented': '', # 代表机构的名称
          'AgencyIR': 0.0075, # 设定(出牌)机构利率， 机构包括 银行 和 第三方支付平台
          'AgencyFR': 0.0025, # 设定机构费率
          'AgencyLR': 0.075, # 设定机构贷款利率，第三方支付平台没有这项
        }
      ],
      # 本轮结果，按选手排列
      'GameResults': [
        {
          'StudentName': '', # 学生(竞赛选手)名称
          'StudentNameID': '', # 学生(竞赛选手)学号
          'Role': '', # 银行，还是 第三方支付平台
          'AgencyRepresented': '', # 代表机构的名称
          'ClientNum': 19, # 留存客户数
          'Cash': 1341, # 现金流结余
          'Profit': 34, # 利润
        }
      ]
    }
  ]

  pass

# 竞赛枚举
class GameEnum():
  SingleRoundGame= SingleRoundGame
  MultiRoundGame= MultiRoundGame
  FreeBattleGame= FreeBattleGame

# 竞赛评估
class GameAssessment():
  GameType: str # 竞赛类型： 单轮对抗SingleRound, 多轮博弈MultiRound, 自由搏击FreeBattle
  Game: GameEnum
  TeamScore: list=[
    {
      'TeamName': str, # 组名
      'TeamAvatar': str, # link to 团队头像图片，如果有的话
      'TeamScore': float, # 小组得分
      'TeamMembers': [] # 小组成员名称列表
    }
  ]

  pass

# 学生评价
class StudentAssessment():
  User: User # 学生
  TotalWholeScore: float # 总分
  TheoryScore: dict={
    'TotalScore': float, # 总分
    # 各个知识点分项得分
    'SubitemScore': [
      {
        'KnowledgeSN': str, # 知识点序号， 排序用
        'KnowledgePoint': str, # 知识点
        'CompletionPercentage': float, # 完成度百分比
        'Score': float, # 知识点得分
      }
    ]
  }
  GameScore: dict={
    'TotalScore': float, # 总分
    'SubitemScore': [
      {
        'GameType': str, # 竞赛类型名称
        'CompletionNum': int, # 完成次数
        'AvgScore': float, # 平均得分
      }
    ]
  }
  pass

# 成就徽章
class AchievementBadge():
  Name: str # 徽章名称
  Avatar: str # link to 徽章图片

# 小组评价
class TeamAssessment():
  Class: Class # 班级
  TeamTemplate: TeamTemplate # 班级内的分组模板
  TeamName: str # 小组名称
  GameCompletionNum: int # 完成竞赛数
  TeamAvgScore: float # 平均得分
  GameList: list=[
    {
      'GameName': str, # 竞赛名称
      'GameType': str, # 竞赛类型
      'GameDuration': int, # 竞赛用时
      'GameScore': float, # 竞赛得分
    }
  ]
  pass

