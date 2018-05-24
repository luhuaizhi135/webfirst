'use strict';

(function($){

  $(function() {

    var datascource = {
      'name': '李克信',
      'title': 'CEO',
      'children': [
        { 'name': '程耿', 'title': '基础设施运维经理', 'className': 'middle-level',
          'children': [
            { 'name': '赵斌', 'title': '电力主管', 'className': 'product-dept' ,
			'children': [
                { 'name': '邹益', 'title': '电力工程师', 'className': 'pipeline1' },
                { 'name': 'Xuan Xuan', 'title': 'engineer', 'className': 'pipeline1' }
              ]},
            { 'name': '张东', 'title': '暖通主管', 'className': 'product-dept',
              'children': [
                { 'name': '周宗兵', 'title': '暖通工程师', 'className': 'pipeline1' },
                { 'name': 'Xuan Xuan', 'title': 'engineer', 'className': 'pipeline1' }
              ]
            }
          ]
        },
        { 'name': '逯怀智', 'title': 'IT运维经理', 'className': 'middle-level',
          'children': [
            { 'name': '韩双巍', 'title': 'IT工程师', 'className': 'rd-dept' },
            { 'name': '陈希阳', 'title': 'IT工程师', 'className': 'rd-dept'}
          ]
        }
      ]
    };

    $('#chart-container').orgchart({
      'data' : datascource,
      'nodeContent': 'title'
    });

  });

})(jQuery);