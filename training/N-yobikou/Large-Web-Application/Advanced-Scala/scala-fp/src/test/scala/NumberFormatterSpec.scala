import org.scalatest.{DiagrammedAssertions, FlatSpec}
import NumberFormatter.format

class NumberFormatterSpec extends FlatSpec with DiagrammedAssertions{

  "format関数" should "整数を取得し、3桁ごとにカンマ区切りを入れた文字列を返す" in {
    assert(format(123456) === "123,456")
    assert(format(1234) === "1,234")
    assert(format(123) === "123")
    assert(format(1234567) === "1,234,567")
    assert(format(-123) === "-123")
    assert(format(-1234567) === "-1,234,567")
    assert(format(0) === "0")
  }
}
