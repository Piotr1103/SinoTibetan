from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def my_date(form):
	import datetime
	now = datetime.datetime.now()

	return now.strftime(form)

# 将词条美观呈现的标签模板
@register.simple_tag
def bodhan(b1, b2, word, han, pronunciation, explanation, create_time):
	# 删除掉讨人厌的、多余的tzinfo和秒数小数点之后的位数
	from re import sub
	create_time = sub(r'\..*$', '', str(create_time))

	# 为多行字串准备的变数字典
	var = {'b1':b1, 'b2':b2, 'w':word, 'h':han, 'p':pronunciation, 'e':explanation, 'c':create_time}

	el = '''\
		<div class="card bg-light text-dark mb-5">
			<div class="card-header bg-{b1} p-3">
				<h1 class="text-center text-light">{w}</h1>
				<h6 class="text-center text-light">{p}</h6>
			</div>

			<div class="card-header bg-{b2} p-3">
				<h3 class="text-center text-light">{h}</h3>
			</div>

			<div class="card-body">
				<p>{e}</p>
			</div>

			<div class="card-footer container">
				<div class="row">
					<div class="text-right" text-align="right">
						{c}
					</div>
				</div>
			</div>
		</div>\
		'''.format(**var)
	return mark_safe(el)