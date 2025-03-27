from invoke import task


@task
def clean(ctx):
	ctx.run("find . -name \"__pycache__\" -delete")
	ctx.run("find . -name \"*.pyc\" -delete")


@task
def build(ctx):
    ctx.run("./makesite.py")


@task(pre=[build])
def serve(ctx):
    ctx.run("cd _site && python -m http.server")
