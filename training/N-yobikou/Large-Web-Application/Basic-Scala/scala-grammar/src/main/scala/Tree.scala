sealed abstract class Tree
case class Branch(value: Int, left: Tree, right: Tree) extends Tree
case object Empty extends Tree

object BinaryTree {
  def max(tree: Tree): Int = tree match {
    case Empty => Int.MinValue
    case Branch(value, left, right) => scala.math.max(value, scala.math.max(max(left), max(right)))
  }
  def min(tree: Tree): Int = tree match {
    case Empty => Int.MaxValue
    case Branch(value, left, right) => scala.math.min(value, scala.math.min(min(left), min(right)))
  }
  def depth(tree: Tree): Int = tree match {
    case Empty => 0
    case Branch(value, left, right) => 1 + scala.math.max(depth(left), depth(right))
  }
}