## `scaleTo`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `fromX`: The start scale on x-coordinate. (`number`)
- `fromY`: The start scale on y-coordinate. (`number`)
- `toX`: The end scale on x-coordinate. (`number`)
- `toY`: The end scale on y-coordinate. (`number`)

RULES:

- The animation only can be used on the widget with `scale-x` and `scale-y` property.
- The property `fromX` and `fromY` is the start scale on x-coordinate and y-coordinate, please let them as required.

EXAMPLES:

// Example of scaling a circle to specific dimensions
<script setup>
import { Circle } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'
import { usePlayer, useWidget } from '@vue-motion/core'
import { scaleTo } from '@vue-motion/lib'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()
const circle = useWidget()

onMounted(() => {
  useAnimation(circle)
    .animate(scaleTo, {
      duration: 2,
      fromX: 1,    // Starting X scale
      fromY: 1,    // Starting Y scale
      toX: 2,      // Target X scale
      toY: 2       // Target Y scale
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <Circle 
      :widget="circle"
      :radius="50"
      fill-color="blue"
    />
  </Motion>
</template>


---

## `Arc`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `radius`: The radius of the circle. (`number`)
- `from`: The start angle. (`number` ranges [0, 360]) [0]
- `to`: The end angle. (`number` ranges [0, 360]) [360]

RULES:

- `radius` is required.
- `from` and `to` must be in the range of [0, 360].

EXAMPLES:

<script setup>
import { Arc } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Arc
      :x="0" 
      :y="0"
      :radius="100"
      :from="0"
      :to="180"
      fill-color="blue"
    />
  </Motion>
</template>


---

## `discolorateBorderTo`

This is a animation api. The animation is used to change the border color of the widget.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `to`: The last value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

RULES:

- `to` is required, it is the final color.
- The animation only can be used on the widget with `border-color` property.


---

## `NumberAxis`

This is a widget from package `@vue-motion/extension-math` api.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `base-unit`: The unit of a coordinate axis. (`'number' | 'radian' | 'degree'`)
- `interval`: Spacing of axes. (`number`) [100]
- `trend`: Trend function to customize the text of the tag. (`(count: number) => string`) [(count) => count.toString()]
- `font-size`: Font size. (`number`) 
- `font-color`: Font color. (`string`) ['white']
- `domain`: Axis range. (`[number, number]`)
- `tip`: Arrow color. (`string`) ["white"]
- `trim`: Arrow border color . (`string`) ["white"]

EXAMPLES:

<script setup>
import { NumberAxis } from '@vue-motion/extension-math'
import { Motion } from '@vue-motion/lib'
</script>

<template>
  <Motion :width="1600" :height="900">
    <NumberAxis 
      :domain="[-5, 5]"
      :interval="100"
      font-color="white"
      :font-size="20"
    />
  </Motion>
</template>


---

## `grow`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

This animation will gradually create the element from 0 to 1.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]

---

## `Image`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `width`: The width of the rectangle. (`number`)
- `height`: The height of the rectangle. (`number`)
- `href`: The url of image. (`string`)

RULES:

- The properties `width`, `height` and `href` are required.
- The `href` property must be a valid image URL or data URL.

EXAMPLES:

<script setup>
import { Image } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Image
      :x="0"
      :y="0"
      :width="300"
      :height="200"
      href="https://example.com/image.png"
    />
  </Motion>
</template>


---

## `destory`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

This animation will gradually destroy the element.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]


---

## `Group`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]

RULES:

- The widget <Group> is used when you want to group multiple widgets together.
- The widget <Group> is not a real widget, it is just a container for other widgets. The slots will contain the children widgets.


---

## `moveTo`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `fromX`: The start x-coordinate. (`number`)
- `fromY`: The start y-coordinate. (`number`)
- `toX`: The end x-coordinate. (`number`)
- `toY`: The end y-coordinate. (`number`)

RULES:

- The animation only can be used on the widget with `x` and `y` property.
- The animation will be used on the widget that has the same level with the widget that you want to animate.

EXAMPLES:

// Example of moving a circle from one point to another
<script setup>
import { Circle } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'
import { usePlayer, useWidget } from '@vue-motion/core'
import { moveTo } from '@vue-motion/lib'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()
const circle = useWidget()

onMounted(() => {
  useAnimation(circle)
    .animate(moveTo, {
      duration: 2,
      fromX: -200,  // Starting X position
      fromY: -200,  // Starting Y position
      toX: 200,     // Ending X position
      toY: 200      // Ending Y position
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <Circle 
      :widget="circle"
      :radius="50"
      fill-color="blue"
    />
  </Motion>
</template>

---

## `MathFunction`

This is a widget from package `@vue-motion/extension-math` api.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fn`: Mathematical function. (`(x: number) => number`)
- `domain`: The domain of the function, that is, the range of x. (`[number, number]`)
- `ranges`: An optional y range that controls the upper and lower limits of the drawing. (`[number, number]`) [[0,0]]
- `division-x`: Calculate the X-axis step size. (`number`) [100]
- `division-y`: Calculate the Y-axis step size. (`number`) [100]
- `color`: Control the color of the graphics. (`string`) ['white']
- `width`: Control the line width of the graph. (`number`) 
- `fill-color`: Controls the fill color of the graph. (`string`) ["none"]

RULES:

- `fill-color` is not be suggested to set, because it is a function image.
- property `domain` has a division effect on the graph, the default value of `division-x` is 100, which means the concrete length of a unit of `domain` is 100. for example if you want to draw a function that's domain is [0, 10], the concrete length will be 10 * 100 = 1000. Don't set the value overloaded otherwise it will render slowly.
- The widget will never to be the children component of other widget (such as <NumberPlane>), if you want to use it as same, please let they to the same level.
- The property that you need to set is `fn`, NOT `function` or `expression` or more.

EXAMPLES:

1. Gradually draw a function

The widget must to be used with `<NumberPlane>` widge and `trace` animation.

<script setup>
import { MathFunction, NumberPlane } from '@vue-motion/extension-math'
import { Motion, trace } from '@vue-motion/lib'
import { usePlayer, useWidget } from '@vue-motion/core'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()

const func = useWidget()
onMounted(() => {
  useAnimation(func)
    .animate(trace, {
      duration: 2
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <NumberPlane :domain-x="[-5, 5]" :domain-y="[-5, 5]" />
    <MathFunction :fn="x => x * x" :widget="func" />
  </Motion>
</template>

2. Change values of some parameters to change the graph

This example is to change the values of `a` and `b` to change the graph.

<script setup>
import { MathFunction, NumberPlane } from '@vue-motion/extension-math'
import { Motion, trace } from '@vue-motion/lib'
import { usePlayer, useWidget, defineAnimation } from '@vue-motion/core'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()

const a = ref(1)
const b = ref(2)

const trans = defineAnimation((target, context) => {
  return (propgress) => {
    target.a = a.value * propgress * 10
    target.b = b.value * propgress * 10
  }
})

const func = useWidget()
onMounted(() => {
  useAnimation(func)
    .animate(trace, {
      duration: 2
    })
    .animate(trans, {
      duration: 5
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <NumberPlane :domain-x="[-5, 5]" :domain-y="[-5, 5]" />
    <MathFunction :fn="x => a * (x - b) * (x - b)" :widget="func" />
  </Motion>
</template>

---

## `Text`

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]- `font_family`: The font family of the text. (`string`) [""]
- `font-size`: The font size of the text. (`'xx-small' | 'x-small' | 'small' | 'medium' | 'large' | 'x-large' | 'xx-large' | 'xxx-large' | 'larger' | 'smaller' | string | number`) [""]
- `font-weight`: The weight of the font. (`number | 'normal' | 'bold' | 'bolder' | 'lighter'`) ['normal']
- `font-style`: The style of the font. (`'normal' | 'italic' | 'oblique'`) ['normal']
- `align`: The horizontal alignment of the text. (`'start' | 'middle' | 'end'`) ['start']
- `baseline`: The vertical alignment of the text. (`'top' | 'middle' | 'bottom'`) ['middle']
- `decoration`: The decoration applied to the text. (`'none' | 'underline' | 'overline' | 'line-through' | 'blink'`) ['none']
- `word-spacing`: The space between words. (`number`) [0]
- `letter-spacing`: The space between letters. (`number`) [0]

EXAMPLES:

<script setup>
import { Text } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Text 
      :x="0"
      :y="0"
      font-size="40"
      fill-color="white"
    >Hello world!</Text>
  </Motion>
</template>

---

## `rotate`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offset`: The offset angle. (`number`)

RULES:

- The animation only can be used on the widget with `rotation` property.
- The property `offset` is the difference between the original angle and the target angle, NOT the target angle.

EXAMPLES:

// Example of rotating a rectangle by 90 degrees
<script setup>
import { Rect } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'
import { usePlayer, useWidget } from '@vue-motion/core'
import { rotate } from '@vue-motion/lib'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()
const rect = useWidget()

onMounted(() => {
  useAnimation(rect)
    .animate(rotate, {
      duration: 2,
      offset: 90  // Rotate 90 degrees clockwise
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <Rect 
      :widget="rect"
      :width="100"
      :height="50"
      fill-color="blue"
    />
  </Motion>
</template>


---

## `Line`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `from`: The start point of the line. (`[number, number]`)
- `to`: The end point of the line. (`[number, number]`)

RULES:

- The property `x` and `y` is the original point of the coordinate system.
- The property `from` and `to` is the start point and end point of the line, please let them as required.

EXAMPLES:

<script setup>
import { Line } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Line
      :from="[-100, -100]"
      :to="[100, 100]"
      border-color="white"
      :border-width="2"
    />
  </Motion>
</template>


---

## `rotateTo`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `from`: The start angle. (`number`)
- `to`: The end angle. (`number`)

RULES:

- The animation only can be used on the widget with `rotation` property.
- The property `from` and `to` is the start angle and end angle, please let them as required.

EXAMPLES:

// Example of rotating a rectangle to a specific angle
<script setup>
import { Rect } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'
import { usePlayer, useWidget } from '@vue-motion/core'
import { rotateTo } from '@vue-motion/lib'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()
const rect = useWidget()

onMounted(() => {
  useAnimation(rect)
    .animate(rotateTo, {
      duration: 2,
      from: 0,    // Starting angle
      to: 180     // Target angle (half rotation)
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <Rect 
      :widget="rect"
      :width="100"
      :height="50"
      fill-color="blue"
    />
  </Motion>
</template>


---

## `Polygon`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `font_family`: The font family of the text. (`string`) [""]
- `points`: The points composing the polygon. (`Array<[number, number]>`)

RULES:

- The property `points` is required, and the value must be an array of points.
- The property `x` and `y` is the original point of the coordinate system.

EXAMPLES:

<script setup>
import { Polygon } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Polygon
      :points="[
        [0, 0],
        [100, 0],
        [100, 100],
        [0, 100]
      ]"
      fill-color="purple"
    />
  </Motion>
</template>


---

## `Webview`

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `width`: The width of the rectangle. (`number`)
- `height`: The height of the rectangle. (`number`)

RULES:

- The properties `width` and `height` are required.
- This component renders a web page within the animation.

EXAMPLES:

<script setup>
import { Webview } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Webview
      :x="0"
      :y="0"
      :width="800"
      :height="600"
    >
      <div>Hello world!</div>
    </Webview>
  </Motion>
</template>



---

## `NumberPlane`

This is a widget from package `@vue-motion/extension-math` api.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `domain-x`: X axis range. (`[number, number]`)
- `domain-y`: Y axis range. (`[number, number]`)
- `interval-x`: X axis interval. (`number`) [100]
- `intervalY`: Y axis interval. (`number`) [100]
- `trend-x`: X axis label trend function. (`(count: number) => string`) [(count) => count.toString()]
- `trend-y`: Y axis label trend function. (`(count: number) => string`) [(count) => count.toString()]
- `font-color-x`: X axis font color. (`string`) ["white"]
- `font-color-y`: Y axis font color. (`string`) ["white"]
- `font-size-x`: X axis font size. (`number`) 
- `font-size-y`: Y axis font size. (`number`) 
- `grid`: Show grid. (`boolean`) [false]
- `grid-color`: Grid color. (`string`) ["white"]
- `grid-width`: Grid line width. (`number`) [1]
- `tip-x`: X axis arrow color. (`string`) ["white"]
- `tip-y`: Y axis arrow color. (`string`) ["white"]
- `base-unit`: The unit of a coordinate axis. (`'number' | 'radian' | 'degree'`)
- `y-rotation`: Control the rotation Angle of Y-axis text. (`number` ranges [0, 360]) [90]

RULES:

- property `domain-x` and `domain-y` has a division effect on the graph, the default value of `interval-x` and `interval-y` is 100, which means the concrete length of a unit of `domain` is 100. for example if you want to draw a function that's domain is [0, 10], the concrete length will be 10 * 100 = 1000. Don't set the value overloaded otherwise it will render slowly.


---

## `move`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offsetX`: The offset on x-coordinate. (`number`)
- `offsetY`: The offset on y-coordinate. (`number`)

RULES:

- The animation only can be used on the widget with `x` and `y` property.
- The animation will be used on the widget that has the same level with the widget that you want to animate.

EXAMPLES:

// Example of moving a circle 200 units right and 100 units up
<script setup>
import { Circle } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'
import { usePlayer, useWidget } from '@vue-motion/core'
import { move } from '@vue-motion/lib'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()
const circle = useWidget()

onMounted(() => {
  useAnimation(circle)
    .animate(move, {
      duration: 2,
      offsetX: 200,  // Move 200 units right
      offsetY: -100  // Move 100 units up
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <Circle 
      :widget="circle"
      :radius="50"
      fill-color="blue"
    />
  </Motion>
</template>


---

## `discolorateFillTo`

This is a animation api. The animation is used to change the fill color of the widget.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `to`: The last value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

RULES:

- `to` is required, it is the final color.
- The animation only can be used on the widget with `fill-color` property.


---

## `PolarPlane`

This is a widget from package `@vue-motion/extension-math` api.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `radius`: The radius of the polar coordinate system. (`[number, number]`)
- `interval`: Angular intervals, used to draw arcs.. (`number`) [100]
- `trend`: Trend function to calculate the Angle trend function. (`(count: number) => string`) [(count) => count.toString()]
- `azimuth-units`: Angular unit. (`'PI radians' | 'TAU radians' | 'degrees' | 'gradians'`) 
- `divide`: Controls how many parts of the polar coordinate plane are divided. (`number`) [20]
- `font-size`: Font size. (`number`) 
- `font-color`: Font color. (`string`) ['white']

RULES:

- The property `radius` is required and defines the size of the polar coordinate system.
- The property `divide` controls the number of radial divisions.
- The property `interval` controls the spacing between circular arcs.

EXAMPLES:

<script setup>
import { PolarPlane } from '@vue-motion/extension-math'
import { Motion } from '@vue-motion/lib'
</script>

<template>
  <Motion :width="1600" :height="900">
    <PolarPlane
      :radius="[0, 500]"
      :divide="12"
      :interval="50"
      font-color="white"
      :font-size="20"
    />
  </Motion>
</template>


---

## `Video`

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `href`: The URL of the video. (`string`)
- `from`: The start time of the video. (`number`)
- `to`: The end time of the video. (`number`)
- `loop`: Whether the video is looped. (`boolean`) [false]
- `auto-play`: Whether the video is autoplayed. (`boolean`) [false]
- `fps`: The frame rate of the video. (`number`) [60]

EXAMPLES:

<script setup>
import { Video } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Video
      :x="0"
      :y="0"
      href="https://example.com/video.mp4"
      :from="0"
      :to="10"
      :auto-play="true"
    />
  </Motion>
</template>


---

## `Tex`

This is a widget from package `@vue-motion/extension-math` api.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `katex-options`: Configuration options to pass to katex rendering. (`katex.KatexOptions`)
- `auto-center`: Whether the formula is automatically centered to render. (`boolean`)

RULES:

- The property `katex-options` is required, and the value must be a katex options.

EXAMPLES:

<script setup>
import { Tex } from '@vue-motion/extension-math'
import { Motion } from '@vue-motion/lib'
</script>

<template>
  <Motion :width="1600" :height="900">
    <Tex
      :katex-options="{
        displayMode: true,
        throwOnError: false
      }"
    >
      f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-itx}dt
    </Tex>
  </Motion>
</template>



---

## `Circle`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `radius`: The radius of the circle. (`number`)

RULES:

- `radius` is required.

EXAMPLES:

<script setup>
import { Circle } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Circle
      :x="0"
      :y="0" 
      :radius="100"
      fill-color="red"
    />
  </Motion>
</template>


---

## `discolorateFill`

This is a animation api. The animation is used to change the fill color of the widget.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offset`: The offset value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

RULES:

- `offset` is required, it is the difference of the color, not the final color.
- The animation only can be used on the widget with `fill-color` property.


---

## `fadeIn`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]


---

## `TextUnit`

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]- `font_family`: The font family of the text. (`string`) [""]
- `font-size`: The font size of the text. (`'xx-small' | 'x-small' | 'small' | 'medium' | 'large' | 'x-large' | 'xx-large' | 'xxx-large' | 'larger' | 'smaller' | string | number`) [""]
- `font-weight`: The weight of the font. (`number | 'normal' | 'bold' | 'bolder' | 'lighter'`) ['normal']
- `font-style`: The style of the font. (`'normal' | 'italic' | 'oblique'`) ['normal']
- `align`: The horizontal alignment of the text. (`'start' | 'middle' | 'end'`) ['start']
- `baseline`: The vertical alignment of the text. (`'top' | 'middle' | 'bottom'`) ['middle']
- `decoration`: The decoration applied to the text. (`'none' | 'underline' | 'overline' | 'line-through' | 'blink'`) ['none']
- `word-spacing`: The space between words. (`number`) [0]
- `letter-spacing`: The space between letters. (`number`) [0]

RULES:

- The text content should be provided as the default slot.
- Font properties like size, weight, and style can be combined for text formatting.
- This component must be used in the `<Text>` component.

EXAMPLES:

<script setup>
import { TextUnit } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'
</script>

<template>
  <Motion :width="1600" :height="900">
    <Text>
      <TextUnit
        :x="0"
        :y="0"
        font-size="40"
        font-weight="bold"
        fill-color="red"
        align="middle"
      >
        Hello
      </TextUnit>
      <TextUnit
        :x="0"
        :y="0"
        font-size="40"
        font-weight="bold"
        fill-color="purple"
        align="middle"
      >
        Hello
      </TextUnit>
    </Text>
  </Motion>
</template>

---

## `fadeOut`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]


---

## `fadeTo`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `from`: The start opacity. (`number`)
- `to`: The end opacity. (`number`)


---

## `moveOnFunction`

This is a animation api. The `moveOnFunction` animation is used to move the widget on the mathematical function.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `path`: The function. (`(progress: number) => { x: number, y: number }`)

RULES:

- The animation only can be used on the widget with `x` and `y` property.
- The animation will be used on the widget that has the same level with the widget that you want to animate.

---

## `scale`

This is a animation api.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offsetX`: The scale value on x-coordinate. (`number`)
- `offsetY`: The scale value on y-coordinate. (`number`)

RULES:

- The animation only can be used on the widget with `scale-x` and `scale-y` property.
- The property `offsetX` and `offsetY` is the difference between the original scale and the target scale, NOT the target scale.

EXAMPLES:

// Example of scaling a circle to twice its size
<script setup>
import { Circle } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'
import { usePlayer, useWidget } from '@vue-motion/core'
import { scale } from '@vue-motion/lib'
import { onMounted } from 'vue'

const { useAnimation, play } = usePlayer()
const circle = useWidget()

onMounted(() => {
  useAnimation(circle)
    .animate(scale, {
      duration: 2,
      offsetX: 1,  // Increase X scale by 1 (double size)
      offsetY: 1   // Increase Y scale by 1 (double size)
    })
  play()
})
</script>

<template>
  <Motion :width="1600" :height="900">
    <Circle 
      :widget="circle"
      :radius="50"
      fill-color="blue"
    />
  </Motion>
</template>


---

## `discolorateBorder`

This is a animation api. The animation is used to change the border color of the widget.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offset`: The offset value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

RULES:

- `offset` is required, it is the difference of the color, not the final color.
- The animation only can be used on the widget with `border-color` property.


---

## `moveOnPath`

This is a animation api. The `moveOnPath` animation is used to move the widget on the SVG path.

API:

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `path`: The SVG path. (`string`)

RULES:

- The animation only can be used on the widget with `x` and `y` property.
- The animation will be used on the widget that has the same level with the widget that you want to animate.

---

## `Ellipse`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `radius`: The radius of the circle. (`number`)
- `cx`: The x-coordinate of the center of the ellipse. (`number`)
- `cy`: The y-coordinate of the center of the ellipse. (`number`)
- `rx`: The x-radius of the ellipse. (`number`)
- `ry`: The y-radius of the ellipse. (`number`)

RULES:

- The properties `cx`, `cy`, `rx`, and `ry` are required.
- The property `radius` is optional and will override `rx` and `ry` if specified.

EXAMPLES:

<script setup>
import { Ellipse } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Ellipse
      :cx="0"
      :cy="0"
      :rx="200"
      :ry="100"
      fill-color="green"
    />
  </Motion>
</template>


---

## `trace`

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

This animation will gradually change the stroke of the element.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]


---

## `Rect`

This is a widget from package `@vue-motion/lib`.

API:

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `width`: The width of the rectangle. (`number`)
- `height`: The height of the rectangle. (`number`)
- `radius`: The radius of the rectangle's four summits. (`number`)

RULES:

- The property `width` and `height` is required, and the value must be a number.
- The property `x` and `y` is the corner of left-top of the rectangle.

EXAMPLES:

<script setup>
import { Rect } from '@vue-motion/lib'
import { Motion } from '@vue-motion/lib'

</script>

<template>
  <Motion :width="1600" :height="900">
    <Rect
      :x="0"
      :y="0"
      :width="200"
      :height="100"
      :radius="10"
      fill-color="orange"
    />
  </Motion>
</template>


---

