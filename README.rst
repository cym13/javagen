Description
===========

Java is tedious to write by hand so here's a little getter/setter generator.

The code is ugly but it works.

Usage
=====

::

    Usage: javagen [-h] [-g] [-s] [-t] [-c classname] (TYPE ATT)...

    Arguments:
        TYPE    Attribute type
        ATT     Attribute name

    Options:
        -g, --getters           Generate getters
        -s, --setters           Generate setters
        -t, --tostring          Generate toString method
        -c, --class classname   Name of the class

Example
=======

::

    $ javagen -gs int age String name
        private int age;
        private String name;

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }


Dependencies
============

Python3 and docopt that you can install with 'pip install docopt'

License
=======

This program is under the GPLv3 License.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

Author
======

::

    Main developper: Cédric Picard
    Email:           cedric.picard@efrei.net
