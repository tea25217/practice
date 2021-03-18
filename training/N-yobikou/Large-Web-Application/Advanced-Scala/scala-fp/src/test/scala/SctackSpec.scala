import org.scalatest._

class StackSpec extends FlatSpec with DiagrammedAssertions {

  "スタック" should "入れた順番の逆に取得できる" in {
    val stack = Stack()
    val stackPushed1 = stack.push(1)
    val stackPushed2 = stackPushed1.push(2)
    val (poped2, stackPoped2) = stackPushed2.pop
    val (poped1, stackPoped1) = stackPoped2.pop

    assert(poped2 === 2)
    assert(poped1 === 1)
  }

  "isEmpty関数" should "正しく空であるかを返す" in {
    val stack = Stack()
    assert(stack.isEmpty === true)
    val stackPushed1 = stack.push(1)
    assert(stackPushed1.isEmpty === false)
    val (_, stackPoped1) = stackPushed1.pop
    assert(stackPoped1.isEmpty === true)
  }

  "空のスタック" should "popをすると例外が発生する" in {
    intercept[IllegalArgumentException] {
      Stack().pop
    }
  }

}