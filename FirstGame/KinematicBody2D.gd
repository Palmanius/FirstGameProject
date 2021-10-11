extends KinematicBody2D


# Declare member variables here. Examples:
# var a = 2
var velocity = Vector2()
var screen_size = Vector2()
var sprite_buffer = Vector2()

# Called when the node enters the scene tree for the first time.
func _ready():
	screen_size = get_viewport_rect().size
	sprite_buffer = Vector2((($AnimatedSprite.scale.x * $AnimatedSprite.frames.get_frame("stationary", 0).get_width()) / 2),(($AnimatedSprite.scale.y * $AnimatedSprite.frames.get_frame("stationary", 0).get_height()) / 2))
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta):
	
	velocity = Vector2()
		
	if Input.is_action_pressed("ui_left"):
		velocity.x -= 1

	elif Input.is_action_pressed("ui_right"):
		velocity.x += 1

	if Input.is_action_pressed("ui_down"):
		velocity.y += 1

	elif Input.is_action_pressed("ui_up"):
		velocity.y -= 1

	if velocity.y == -1:
		if velocity.x == 1:
			$AnimatedSprite.rotation_degrees = 45
			$AnimatedSprite.animation = "forward"
			$AnimatedSprite.play()
		elif velocity.x == -1:
			$AnimatedSprite.rotation_degrees = -45
			$AnimatedSprite.animation = "forward"
			$AnimatedSprite.play()
		else:
			$AnimatedSprite.rotation_degrees = 0
			$AnimatedSprite.animation = "forward"
			$AnimatedSprite.play()
	else:
		$AnimatedSprite.rotation_degrees = 0
		$AnimatedSprite.animation = "stationary"
		$AnimatedSprite.stop()
		
	velocity = velocity.normalized() * 200
		
	position += velocity * delta
	
	position.x = clamp(position.x, 0 + sprite_buffer.x, screen_size.x - sprite_buffer.x)
	position.y = clamp(position.y, 0 + sprite_buffer.y, screen_size.y - sprite_buffer.y)
